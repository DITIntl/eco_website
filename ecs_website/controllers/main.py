# -*- coding: utf-8 -*-
from odoo import http


class RouteWebsite(http.Controller):
    @http.route('/ecosoft/', auth='public', website=True)
    def index(self, **kw):
        email_subscribe = kw.get('contact_email', False)
        if email_subscribe:
            http.request.env['subscribe.post'].create(kw)
        return http.request.render('ecs_website.index')

    @http.route('/contact', auth='public', website=True)
    def contact(self, **kw):
        inform = kw.get('name', False)
        if inform:
            http.request.env['customer.contact'].create(kw)
        return http.request.render('ecs_website.ecs_contact')
