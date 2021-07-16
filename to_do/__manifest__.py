# -*- coding: utf-8 -*-
{
    'name': "to_do",

    'summary': """
        Tasks to do""",
    'sequence': -100,

    'description': """
        A database of tasks
    """,

    'author': "Graco Silva",
    'website': "http://www.example.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
