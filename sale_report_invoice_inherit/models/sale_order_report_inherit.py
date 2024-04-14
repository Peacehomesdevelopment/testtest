from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoice_lines = fields.One2many(
        'account.move.line', 'sale_order_id',
        string='Invoice Lines',
        compute='_compute_invoice_lines',
        store=True
    )

    @api.depends('line_ids', 'payment_term_id')
    def _compute_invoice_lines(self):
        for order in self:
            order.invoice_lines = order.line_ids.filtered(
                lambda line: line.payment_term_id == order.payment_term_id
            )[:1]
