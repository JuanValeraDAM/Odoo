# -*- coding: utf-8 -*-
{
    'name': "milibro",
    'sequence': 0,

    'summary': """
        Descripción corta de mi primer módulo en Odoo""",

    'description': """
       Descripción larga de mi primer módulo en Odoo
    """,

    'author': "Juan Valera",
    'website': "http://www.ieschirinos.com",

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
        'views/libro.xml',
        'views/autor.xml',
        'views/editorial.xml',
        'views/categoria.xml',
        'views/cdu.xml',
        'views/ejemplar.xml',
        'views/prestamo.xml',
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
