import base64
from io import BytesIO
import qrcode

from account_payment_instalment import models

class QRCodeGenerator(models.AbstractModel):
    _name = 'qr_code_generator'

    @api.model # type: ignore
    def _generate_base_url(self, record):
        # Generate the base URL for the payment
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        if not 'localhost' in base_url:
            if 'http://' in base_url:
                base_url = base_url.replace('http://', 'https://')
        base_url = base_url + '/web#id=' + str(record.id) + '&model=' + record._name + '&view_type=form&cids='
        return base_url

    @api.model # type: ignore
    def _generate_qr_code_image(self, record, base_url):
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
        # Get the 'qr_code_generator' model
        qr_generator = self.env['qr_code_generator']

        # Loop through each payment record
        for record in self:
            # Generate the base URL for the payment
            base_url = qr_generator._generate_base_url(record)

            # Generate the QR code image
            qr_code_img = qr_generator._generate_qr_code_image(record, base_url)

            # Convert the image to binary data and store it in the 'qr_code' field
            record.qr_code = qr_generator._convert_image_to_binary(record, qr_code_img)
        
@api.depends('recipient_name', 'amount', 'payment_description') # type: ignore
def _compute_qr_code(self):
    """
    Compute the QR code for each record based on recipient details and payment information.

    This method iterates through each record, generates the base URL and QR code image,
    and stores the binary representation of the image in the 'qr_code' field.

    Args:
        self: RecordSet of 'account.payment' model.

    Returns:
        None
    """
    _logger = self.env['account.payment'].sudo()._logger
    _logger.debug("Computing QR code for account.payment records...")
    # Iterate through each record
    for record in self:
        _logger.debug(f"Computing QR code for record {record.id}")
        # Generate the base URL for the payment
        base_url = record._generate_base_url()
        _logger.debug(f"Generated base URL: {base_url}")

        # Generate the QR code image
        qr_code_img = record._generate_qr_code_image(base_url)
        _logger.debug("Generated QR code image")

        # Convert the image to binary data and store it in the 'qr_code' field
        record.qr_code = self._convert_image_to_binary(qr_code_img)
        _logger.debug(f"Stored binary representation of QR code in 'qr_code' field of record {record.id}")

