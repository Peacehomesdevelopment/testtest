from odoo import models, fields


class FieldWidgets(models.Model):
    """We can't filter a selection field dynamically
       so when we select a field its widgets also need to change according to the selected
       field type, we can't do it by a 'selection' field, need a 'Many2one' field.
    """

    _name = 'dynamic.field.widgets'
    _rec_name = 'description'
    _description = 'Field Widgets'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
