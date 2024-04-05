import unittest
from unittest.mock import Mock
from odoo.tests.common import TransactionCase

class TestComputeQRCode(TransactionCase):

    def test_generate_base_url(self):
        # Create a mock record
        record = Mock()
        
        # Mock the _generate_base_url method
        record._generate_base_url = Mock(return_value="https://example.com/payment")
        
        # Call the _compute_qr_code method
        record._compute_qr_code()
        
        # Assert that the _generate_base_url method was called
        record._generate_base_url.assert_called_once()

    def test_generate_qr_code_image(self):
        # Create a mock record
        record = Mock()
        
        # Mock the _generate_base_url method
        record._generate_base_url = Mock(return_value="https://example.com/payment")
        
        # Mock the _generate_qr_code_image method
        record._generate_qr_code_image = Mock(return_value="mocked_qr_code_image")
        
        # Call the _compute_qr_code method
        record._compute_qr_code()
        
        # Assert that the _generate_qr_code_image method was called with the correct base URL
        record._generate_qr_code_image.assert_called_once_with("https://example.com/payment")

    def test_convert_image_to_binary(self):
        # Create a mock record
        record = Mock()
        
        # Mock the _generate_base_url method
        record._generate_base_url = Mock(return_value="https://example.com/payment")
        
        # Mock the _generate_qr_code_image method
        record._generate_qr_code_image = Mock(return_value="mocked_qr_code_image")
        
        # Mock the _convert_image_to_binary method
        record._convert_image_to_binary = Mock(return_value=b"mocked_binary_data")
        
        # Call the _compute_qr_code method
        record._compute_qr_code()
        
        # Assert that the qr_code field was set with the binary data
        self.assertEqual(record.qr_code, b"mocked_binary_data")

if __name__ == '__main__':
    unittest.main()