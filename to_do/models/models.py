# -*- coding: utf-8 -*-

from odoo import models, fields, api


class to_do(models.Model):
    _name = 'to_do.to_do'
    _description = 'to_do.to_do'

    name = fields.Char(required=True)
    author = fields.Char(required=True)
    responsable = fields.Char()
    description = fields.Text()
    isFinished = fields.Boolean()
    createdAt = fields.Date(required=True)
    value2 = fields.Float(compute="_value_pc", store=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
