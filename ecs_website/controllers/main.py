# -*- coding: utf-8 -*-
from odoo import http


class RouteWebsite(http.Controller):

    @http.route('/contactus', auth='public', website=True)
    def contact(self, **kw):
        inform = kw.get('name', False)
        if inform:
            http.request.env['customer.contact'].create(kw)
        return http.request.render('ecs_website.contactus')
