from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def instant_publish_product(self):
        self.write({
            'website_published': True
        })

    def instant_unpublish_product(self):
        self.write({
            'website_published': False
        })
