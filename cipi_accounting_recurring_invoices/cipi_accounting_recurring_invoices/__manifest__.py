{
    'name': "cipi_accounting_recurring_invoices",

    'summary': """
        mod accounting """,

    'description': """
        penambahan reason and cancel
    """,

    'author': "hashmicro",
    'website': "http://www.hashmicro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'equip3_accounting_recurring'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_recurring_views.xml',
        'wizard/cancel_form_views.xml',
    ],
    # # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
