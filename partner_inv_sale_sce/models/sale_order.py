from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('partner_id')
    def _compute_partner_invoices(self):
        for order_id in self:
            total_invoiced = 0
            total_billed = 0
            receivable_amount = 0
            payable_amount = 0

            invoice_ids = []
            if order_id.partner_id.id:
                invoice_ids = self.env['account.move'].search(
                    [('partner_id', '=', order_id.partner_id.id),
                     ('move_type', '=', 'out_invoice'),
                     ('state', '=', 'posted')])
            for invoice_id in invoice_ids:
                total_invoiced += invoice_id.amount_total
                receivable_amount += invoice_id.amount_residual

            bill_ids = []
            if order_id.partner_id.id:
                bill_ids = self.env['account.move'].search(
                    [('partner_id', '=', order_id.partner_id.id),
                     ('move_type', '=', 'in_invoice'),
                     ('state', '=', 'posted')])
            for bill_id in bill_ids:
                total_billed += bill_id.amount_total
                payable_amount += bill_id.amount_residual

            order_id.total_invoiced = total_invoiced
            order_id.total_billed = total_billed
            order_id.receivable_amount = receivable_amount
            order_id.payable_amount = payable_amount
            order_id.total_balance = receivable_amount - payable_amount

    total_invoiced = fields.Monetary(
        string='Total Invoiced', compute='_compute_partner_invoices',
        store=True)
    total_billed = fields.Monetary(
        string='Total Billed', compute='_compute_partner_invoices', store=True)
    receivable_amount = fields.Monetary(
        string='To Receive', compute='_compute_partner_invoices', store=True)
    payable_amount = fields.Monetary(
        string='To Pay', compute='_compute_partner_invoices', store=True)
    total_balance = fields.Monetary(
        string='Partner Balance', compute='_compute_partner_invoices',
        store=True)
