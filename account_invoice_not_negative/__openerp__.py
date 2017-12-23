# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2016-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Account invoice not negative',
    'category': 'Account',
    'summary': 'No validate invoices if the total is negative',
    'version': '8.0.1.0.0',
    'description': (
        'New option in journal to allow or not to open invoices with negative '
        'total amount'),
    'author': 'Trey (www.trey.es)',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_journal_view.xml',
    ],
    'installable': True,
}