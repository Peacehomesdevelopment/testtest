# -*- coding: utf-8 -*-
{
    "name": "Sale Order QR",
    "summary": """Sale Order and Quotation QR""",
    'author': "Core48",
    'website': "https://core48.com",
    'license': 'LGPL-3',
    'category': 'sale',
    "version": "17.0.0.2",
    "depends": [
        'sale_management'
            ],
    "data": [
        "views/inherit_sale.xml",
        "views/inherit_report.xml" 
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "images": ["static/description/banner.jpg"],
}
