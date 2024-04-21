from odoo import models, fields


class IrModelFields(models.Model):
    """Adding a new field to understand the dynamically created fields."""

    _inherit = 'ir.model.fields'

    is_dynamic_field = fields.Boolean(string="Dynamic Field")
