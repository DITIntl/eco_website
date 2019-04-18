# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ecosoft Website',
    'category': 'Theme/Creative',
    'description': """
Odoo Web Editor widget.
==========================

""",
    'version': '12.0.1.0.0',
    'author': 'Saran Lim.',
    'depends': [
        'website',
        'website_blog',
        'website_hr_recruitment',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/templates.xml',
        'views/home_page_view.xml',
        'views/our_approach_page_view.xml',
        'views/solutions_page_view.xml',
        'views/training_page_view.xml',
        'views/website_blog_templates.xml',
        'views/job_page_view.xml',
        'views/contact_page_view.xml',
        'views/contact_view.xml',
    ],
    'installable': True,
}
