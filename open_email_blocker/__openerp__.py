# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2014-2016 Openies Services(<http://openies.com>).
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
    "name" : "Openies Email Blocker",
    "version" : "1.0",
    "author" : "Openies Services",
    'website' : 'http://Openies.com',
    "category" : "Account",
    "summary": 'Block or redirect email from Odoo',
    "description": """
Openies Email Blocker
========================================
    A module provides functionality to block or redirect odoo email by changing the config files.
""",
    "license" : "AGPL-3",
    "depends" : ['mail'],
    "data" : [],
    "demo" : [],
    'auto_install': False,
    "installable": True,
    'images': ['static/description/openies_email_blocker.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
