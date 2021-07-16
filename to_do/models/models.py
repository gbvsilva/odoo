# -*- coding: utf-8 -*-

from odoo import models, fields, api


class to_do(models.Model):
    _name = 'to_do.to_do'
    _description = 'to_do.to_do'

    name = fields.Char(required=True)
    author = fields.Char(required=True)
    partner_id = fields.Selection(selection=[('primario', 'Primario'), 
                ('secundario', 'Secundario')], string='Funcao', default='primario')
    description = fields.Text()
    isFinished = fields.Boolean()
    createdAt = fields.Date(required=True)
    