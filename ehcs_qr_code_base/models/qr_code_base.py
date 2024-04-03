import base64
from io import BytesIO
import qrcode

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    qr_code = fields.Binary(string='QR Code', compute='_compute_qr_code', store=True)

    @api.depends('name', 'size')
    def _compute_qr_code(self):
        for record in self:
            base_url = record._generate_base_url()
            qr_code_img = record._generate_qr_code_image(base_url)
            record.qr_code = self._convert_image_to_binary(qr_code_img)

    def _generate_base_url(self):
        # Generate the base URL for the payment
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        if not 'localhost' in base_url:
            if 'http://' in base_url:
                base_url = base_url.replace('http://', 'https://')
        base_url = base_url + '/web#id=' + str(self.id) + '&model=account.payment&view_type=form&cids='
        return base_url

    def _generate_qr_code_image(self, base_url):
        # Generate QR code image
        qr_code = qrcode.QRCode(version=4, box_size=4, border=1)
        qr_code.add_data(base_url)
        qr_code.make(fit=True)
        qr_img = qr_code.make_image()
        return qr_img

    def _convert_image_to_binary(self, qr_code_img):
        # Convert image to binary data
        buffered = BytesIO()
        qr_code_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        return img_str
        
@api.depends('recipient_name', 'amount', 'payment_description')
def _compute_qr_code(self):
    for record in self:
        base_url = record._generate_base_url()
        qr_code_img = record._generate_qr_code_image(base_url)
        record.qr_code = self._convert_image_to_binary(qr_code_img)

