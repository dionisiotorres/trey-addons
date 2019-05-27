# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from .confirming_kutxa import ConfirmingKutxa
from openerp import models, api


class BankingExportCsbWizard(models.TransientModel):
    _inherit = 'banking.export.csb.wizard'

    @api.model
    def _check_company_bank_account(self, payment_order):
        if not payment_order.mode.is_conf_kutxa:
            super(BankingExportCsbWizard, self)._check_company_bank_account(
                payment_order)

    @api.model
    def _check_required_bank_account(self, payment_order, pay_lines):
        if not payment_order.mode.is_conf_kutxa:
            super(BankingExportCsbWizard, self)._check_required_bank_account(
                payment_order, pay_lines)

    @api.model
    def _get_csb_exporter(self, payment_order):
        if payment_order.mode.type.code == 'conf_kutxa':
            csb = ConfirmingKutxa(self.env)
        else:
            csb = super(BankingExportCsbWizard, self)._get_csb_exporter(
                payment_order)
        return csb
