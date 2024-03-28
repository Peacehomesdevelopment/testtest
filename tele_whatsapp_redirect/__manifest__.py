# -*- coding: utf-8 -*-
{
    'name': 'Send Whatsapp Message Odoo17',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Send Message to partner via Whatsapp web',
    'description': 'This module helps you to directly send messages to your '
                   'contacts through WhatsApp web.',
    'author': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'company': 'TeleNoc',
    'website': '',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'wizard/whatsapp_send_message_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
