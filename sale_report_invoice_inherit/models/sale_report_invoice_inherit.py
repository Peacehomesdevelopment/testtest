from odoo import models, fields

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    line_ids = fields.One2many('sale.order.line', 'order_id', string='Order Lines', copy=True, readonly=True, domain=[('display_type', '=', 'line')])
    payment_term_line_ids = fields.One2many('account.payment.term', 'invoice_id', string='Payment Term Line', readonly=True)

    
