# -*- coding: utf-8 -*-
import werkzeug
import base64
import requests
import logging
import odoo.http as http
from odoo.http import request

_logger = logging.getLogger(__name__)


class SupportTicketController(http.Controller):

    @http.route('/support/ticket/submit', type="http",
                auth="user", website=True)
    def support_submit_ticket(self, **kw):
        """Let's public and registered user submit a support ticket"""
        person_name = http.request.env.user.name

        category_access = []
        for category_permission in http.request.env.user.groups_id:
            category_access.append(category_permission.id)

        ticket_categories = http.request.env['project.tags'].sudo().search([])
        setting_google_recaptcha_active = request.env['ir.default'].get(
            'website.support.settings', 'google_recaptcha_active')
        setting_google_captcha_client_key = request.env['ir.default'].get(
            'website.support.settings', 'google_captcha_client_key')

        return http.request.render(
            'ecs_website_support.support_submit_ticket',
            {'categories': ticket_categories,
             'person_name': person_name,
             'email': http.request.env.user.email,
             'setting_google_recaptcha_active':
                setting_google_recaptcha_active,
             'setting_google_captcha_client_key':
                setting_google_captcha_client_key})

    @http.route('/support/ticket/process', type="http", auth="public",
                website=True, csrf=True)
    def support_process_ticket(self, **kwargs):
        """Adds the support ticket to the database and sends out emails to
           everyone following the support ticket category"""
        values = {}
        for field_name, field_value in kwargs.items():
            values[field_name] = field_value

        if values['my_gold'] != "256":
            return "Bot Detected"

        setting_google_recaptcha_active = request.env['ir.default'].get(
            'website.support.settings', 'google_recaptcha_active')

        if setting_google_recaptcha_active:

            setting_google_captcha_secret_key = request.env['ir.default'].get(
                'website.support.settings', 'google_captcha_secret_key')

            # Redirect them back if they didn't answer the captcha
            if 'g-recaptcha-response' not in values:
                return werkzeug.utils.redirect("/support/ticket/submit")

            payload = {'secret': setting_google_captcha_secret_key,
                       'response': str(values['g-recaptcha-response'])}
            response_json = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=payload)

            if response_json.json()['success'] is not True:
                return werkzeug.utils.redirect("/support/ticket/submit")

        create_dict = {}
        customer_id = request.env['res.partner'].sudo().search(
            [('name', '=', values['person_name'])])
        project_id = request.env['project.project'].sudo().search(
            [('project_index', '!=', False)])

        create_dict = {'name': values['subject'],
                       'partner_id': customer_id.id,
                       'email_from': values['email'],
                       'description': values['description'],
                       'tag_ids': [(6, 0, [values['category']])],
                       'project_id': project_id.id}

        new_ticket_id = request.env['project.task'].sudo().create(create_dict)

        if 'file' in values:

            for c_file in request.httprequest.files.getlist('file'):
                data = c_file.read()

                if c_file.filename:
                    request.env['ir.attachment'].sudo().create({
                        'name': c_file.filename,
                        'datas': base64.b64encode(data),
                        'datas_fname': c_file.filename,
                        'res_model': 'project.task',
                        'res_id': new_ticket_id.id
                    })
        return werkzeug.utils.redirect("/support/ticket/thanks")

    @http.route('/support/ticket/thanks', type="http",
                auth="public", website=True)
    def support_ticket_thanks(self, **kw):
        """Displays a thank you page after the user submits a ticket"""
        return http.request.render('ecs_website_support.support_thank_you', {})
