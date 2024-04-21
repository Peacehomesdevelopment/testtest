from odoo import models, fields

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    line_ids = fields.One2many('sale.order.line', 'order_id', string='Order Lines', copy=True, readonly=True, domain=[('display_type', '=', 'line')])
    payment_term_line_ids = fields.One2many('account.payment.term', 'invoice_id', string='Payment Term Line', readonly=True)

    

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "727f4cc3-4374-4b30-919a-9358c3b4a137",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
