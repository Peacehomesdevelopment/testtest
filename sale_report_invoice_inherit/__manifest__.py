{
    'name': 'Custom Sales Report Invoice View Inheritance',
    'version': '1.0',
    'summary': 'Inherit sales report invoice view in sales order',
    'description': 'This module inherits the sales report invoice view in the sales order.',
    'category': 'Sales',
    'author': 'Renbran',
    'website': 'http://www.bpproperties.com',
    'depends': ['sale'],
    'data': [
        'views/sale_order_report_inherit.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
