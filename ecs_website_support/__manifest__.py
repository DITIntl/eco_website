# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ecosoft Website Support',
    'summary': 'Build customized support in your website',
    'category': 'Website',
    'version': '12.0.1.0.0',
    'author': 'Sythil Tech, Adaptive City',
    'depends': [
        'website',
        'project',
        'eco_project_index',
        'website_crm'
    ],
    'data': [
        'data/data.xml',
        'views/website_support_template.xml',
    ],
    'maintainers': ['Saran Lim.'],
    'installable': True,
}
