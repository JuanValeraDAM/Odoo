# -*- coding: utf-8 -*-
{
    'name': "ambulancias",
    'sequence': 0,

    'summary': """
       Descripción corta""",

    'description': """
        Descripción larga
    """,

    'author': "Juan Valera Reales",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/vehiculo.xml',
        'views/marca.xml',
        'views/mantenimiento.xml',
        'views/mantenimiento_linea.xml',
        'views/modelo.xml',
        'views/partner.xml',
        'views/repostaje.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
