# -*- coding: utf-8 -*-
from odoo import models, fields


class CustomerContact(models.Model):
    _name = 'customer.contact'

    name = fields.Char(
        string='Name',
        required=True,
    )
    email = fields.Char(
        string='Email',
        required=True,
    )
    company_name = fields.Char(
        string='Company Name',
        required=True,
    )
    title = fields.Char(
        string='Your Title',
    )
    subject = fields.Char(
        string='Subject',
        required=True,
    )
    message = fields.Text(
        string='Message',
        required=True,
    )
    type_system1 = fields.Char(
        string='What kind of system are you using?',
    )
    type_system2 = fields.Char(
        string='What kind of system are you using?',
    )
    module_interesting = fields.Text(
        string='What module(s) are you interested in?',
    )
    reason = fields.Text(
        string='Reason(s) of finding a new system?',
    )
    solve = fields.Char(
        string='Please prove that you are human by solving the equation',
        required=True,
    )
