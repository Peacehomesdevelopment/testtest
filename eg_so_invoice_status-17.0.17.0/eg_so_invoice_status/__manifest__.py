{
    'name': 'Invoice Status in Sale Order',
    'version': '17.0',
    'category': 'Sale',
    'summery': 'Invoice Status in Sale Order',
    'author': 'INKERP',
    'website': "https://www.INKERP.com",
    'depends': ['sale_management', 'account'],

    'data': [
        'views/sale_order_view.xml',
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
