# -*- coding: utf-8 -*-
# from odoo import http


# class Rent(http.Controller):
#     @http.route('/rent/rent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rent/rent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rent.listing', {
#             'root': '/rent/rent',
#             'objects': http.request.env['rent.rent'].search([]),
#         })

#     @http.route('/rent/rent/objects/<model("rent.rent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rent.object', {
#             'object': obj
#         })
