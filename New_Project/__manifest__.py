{
    'name' : 'Real Estate',
    'version' : '1.0',
    'category': 'Real Estate Property',
    'sequence':'-100',
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/property_menu.xml',
        'views/agent_menu.xml',
        'views/client_menu.xml',
        'demo/real_estate_property_demo.xml',
        'demo/real_estate_client_demo.xml',
        'demo/real_estate_agent_demo.xml',
    ],
    'installable':True,
    'application': True,
    'auto_install': False
}