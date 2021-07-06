# -*- coding: utf-8 -*-

from odoo import models, fields, api


class to-do(models.Model):
    _name = 'to-do.to-do'
    _description = 'to-do.to-do'

    name = fields.Char(required=True)
    author = fields.Char(required=True)
    responsable = fields.Char()
    description = fields.Text()
    isFinished = fields.Boolean()
    createdAt = fields.Date(required=True)
    #value2 = fields.Float(compute="_value_pc", store=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
