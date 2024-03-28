# -*- coding: utf-8 -*-

{
    'name': 'Previous Invoice in Sale Order',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'license': 'LGPL-3',
    'summary': """Previous invoice details of customer in sale form""",
    'depends': [
        'base',
        'sale',
        'sale_management',
        'account',
    ],
    'author': 'SugarClone ERP',
    'support': 'sugarcloneerp@gmail.com',
    'description': """ Updates Below
    - Total sale invoice amount of customer
    - Total purchase bill amount of the partner
    - Total payment to receive from customer
    - Total payable to partner
    """,
    'data': [
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
