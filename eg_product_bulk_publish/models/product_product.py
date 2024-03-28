from odoo import models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def instant_publish_product(self):
        self.write({
            'website_published': True
        })

    def instant_unpublish_product(self):
        self.write({
            'website_published': False
        })
