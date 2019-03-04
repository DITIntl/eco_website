# -*- coding: utf-8 -*-
from odoo import models, fields


class EmailSubscribe(models.Model):
    _name = 'subscribe.post'

    contact_email = fields.Char(
        string='Email',
    )
