from odoo import models, fields, api
import qrcode
import base64
from io import BytesIO

class AccountPayment(models.Model):
    _inherit = "product.template"

    # Assuming 'qr_code' is the field containing the data to encode in the QR code
    qr_code = fields.Char('QR Code')

    # 'qr_image' is the Binary field where the QR code image will be stored
    qr_image = fields.Binary(string="QR Image", attachment=True)

    def generate_qr_code_button(self):
        for record in self:
            # Proceed only if there is data to encode
            if record.qr_code:
                # Set up QR code generation
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(record.qr_code)
                qr.make(fit=True)

                # Generate QR code as an image
                img = qr.make_image(fill_color="black", back_color="white")

                # Save the image to a BytesIO buffer
                temp = BytesIO()
                img.save(temp, format="PNG")
                temp.seek(0)

                # Encode the image in base64 and assign it to 'qr_image' field
                record.qr_image = base64.b64encode(temp.getvalue())
