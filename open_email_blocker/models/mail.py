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

from openerp.tools import config
from openerp import models


class MailServer(models.Model):

    _inherit = 'ir.mail_server'
        
    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
                   context=None):
        mail_data = message.key()
        if config.get('block_email', False):
            return True
        if config.get('redirect_mail', False):
            redirect_address = config.get('redirect_mail')
            if "To" in keys:
                message.replace_header('To', redirect_address)
            if "Cc" in keys:
                message.replace_header('Cc', redirect_address)
            if "Bcc" in keys:
                message.replace_header('Bcc', redirect_address)
        return super(MailServer, self).send_email(cr, uid, message, mail_server_id, smtp_server, smtp_port,
                   smtp_user, smtp_password, smtp_encryption, smtp_debug,context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: