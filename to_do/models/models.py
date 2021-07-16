# -*- coding: utf-8 -*-

from odoo import models, fields, api


class to_do(models.Model):
    _name = 'to_do.to_do'
    _description = 'to_do.to_do'

    name = fields.Char(required=True, string='Title')
    author = fields.Char(required=True, string='Author')
    partner_id = fields.Selection(selection=[('primario', 'Primario'), 
                ('secundario', 'Secundario')], string='Funcao', default='primario')
    description = fields.Text(string='Description')
    isFinished = fields.Boolean(string='isFinished')
    createdAt = fields.Date(required=True, string='createdAt')
    