# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
##############################################################################
{
    'name': 'Ukraine - Chart of accounts',
    'version': '1.2',
    'author': 'golubev',
    'category': 'Localization/Account Charts',
    'description': """
Ukraine - Chart of accounts.
==================================
    """,
    'website': 'http://www.nt.net.ua',
    'depends': ['account_chart'],
    'data': [
        'l10n_ua_account_type.xml',
        'account_chart_template.xml',
        'account.account.template.csv',
        'account_chart_template_after.xml',
        'l10n_ua_wizard.xml',
        'report_invoice.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
