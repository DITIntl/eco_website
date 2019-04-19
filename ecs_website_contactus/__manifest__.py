# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ecosoft Website Contact Form',
    'category': 'Website',
    'summary': 'Generate leads from a contact form',
    'version': '12.0.1.0.0',
    'author': 'Saran Lim.',
    'description': """
        Generate leads or opportunities in the CRM app from a contact form
        published on the Contact us page of your website. This form can be
        customized thanks to the *Form Builder* module
        (available in Odoo Enterprise).
    """,
    'depends': ['website_crm'],
    'data': [
        'views/website_crm_templates.xml',
    ],
    'installable': True,
}
