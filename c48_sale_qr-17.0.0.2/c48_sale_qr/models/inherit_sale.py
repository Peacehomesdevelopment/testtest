from odoo import fields, models

class InheritQuotatins(models.Model):
    _inherit = 'sale.order'

    qr = fields.Binary(string='QR')
