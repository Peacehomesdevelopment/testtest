from odoo import models, fields, api, _

from datetime import datetime, date, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoice_status = fields.Char(string="Invoice Status", compute='_delivery_status')

    @api.onchange('invoice_ids')
    @api.depends('invoice_ids')
    def _delivery_status(self):
        for order in self:
            if order.invoice_ids.mapped('state'):
                status = order.invoice_ids.mapped('payment_state')
                res = all(ele == status[0] for ele in status)
                if res:
                    if status[0] == 'not_paid':
                        order.invoice_status = '📋 Not Paid'
                    elif status[0] in 'paid':
                        order.invoice_status = '📋 Fully Paid'
                    elif status[0] in 'in_payment':
                        order.invoice_status = '📋 In Payment'
                    else:
                        order.invoice_status = '📋 Fully Paid'
                else:
                    if 'paid' in status:
                        order.invoice_status = '📋 Partially Paid'
                    else:
                        order.invoice_status = '📋 To Invoice'
            else:
                order.invoice_status = '📋 No Invoice'
