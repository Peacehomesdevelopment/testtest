import base64
from io import BytesIO
import qrcode

from account_payment import models

class QRCodeGenerator(models.AbstractModel):
    _name = 'qr_code_generator'

    @api.model # type: ignore
    def _generate_base_url(self, record):
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

    @api.model # type: ignore
    def _convert_image_to_binary(self, record, qr_code_img):
        # Convert image to binary data
        buffered = BytesIO()
        qr_code_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        return img_str

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    qr_code = fields.Binary(string='QR Code', compute='_compute_qr_code', store=True) # type: ignore

    @api.depends('name', 'size') # type: ignore
    def _compute_qr_code(self):
        """
        Compute the QR code for each payment record and store it in the 'qr_code' field.
        The QR code is generated using the 'qr_code_generator' model.
        """
        print('--------------------------------------------------------------------')
        print('Computing QR code for {} payment records'.format(len(self)))

        # Get the 'qr_code_generator' model
        qr_generator = self.env['qr_code_generator']

        # Loop through each payment record
        for record in self:
            print('Processing payment record with ID {}'.format(record.id))

            # Generate the base URL for the payment
            # This base URL is used to generate the QR code
            base_url = qr_generator._generate_base_url(record) # type: ignore
            print('Generated base URL: {}'.format(base_url))

            # Generate the QR code image using the base URL
            # The generated QR code is stored in 'qr_code_img'
            qr_code_img = qr_generator._generate_qr_code_image(record, base_url) # type: ignore
            print('Generated QR code image')

            # Convert the QR code image to binary data and store it in the 'qr_code' field of the payment record
            # The converted binary data is the QR code of the payment record
            record.qr_code = qr_generator._convert_image_to_binary(record, qr_code_img) # type: ignore
            print('Converted QR code image to binary data and stored in payment record')
            print('--------------------------------------------------------------------')
<|bot|>
        
@api.multi # type: ignore
def _compute_qr_code(self):
    """
    Generate QR codes for each record in the current object.
    """
    records = list(self)
    qr_generator = self.env['qr_code_generator']
    base_urls = {record.id: qr_generator._generate_base_url(record)
                 for record in records}
    qr_code_imgs = {record.id: record._generate_qr_code_image(base_urls[record.id])
                    for record in records}

    for record in records:
        record.qr_code = self._convert_image_to_binary(
            record, qr_code_imgs[record.id])


