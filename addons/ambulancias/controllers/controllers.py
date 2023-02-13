# -*- coding: utf-8 -*-
# from odoo import http


# class Ambulancias(http.Controller):
#     @http.route('/ambulancias/ambulancias', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ambulancias/ambulancias/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ambulancias.listing', {
#             'root': '/ambulancias/ambulancias',
#             'objects': http.request.env['ambulancias.ambulancias'].search([]),
#         })

#     @http.route('/ambulancias/ambulancias/objects/<model("ambulancias.ambulancias"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ambulancias.object', {
#             'object': obj
#         })
