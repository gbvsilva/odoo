# -*- coding: utf-8 -*-
# from odoo import http


# class Novo(http.Controller):
#     @http.route('/novo/novo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/novo/novo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('novo.listing', {
#             'root': '/novo/novo',
#             'objects': http.request.env['novo.novo'].search([]),
#         })

#     @http.route('/novo/novo/objects/<model("novo.novo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('novo.object', {
#             'object': obj
#         })
