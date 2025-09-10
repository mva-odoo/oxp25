# from odoo import http


# class MyFurniture(http.Controller):
#     @http.route('/my_furniture/my_furniture', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_furniture/my_furniture/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_furniture.listing', {
#             'root': '/my_furniture/my_furniture',
#             'objects': http.request.env['my_furniture.my_furniture'].search([]),
#         })

#     @http.route('/my_furniture/my_furniture/objects/<model("my_furniture.my_furniture"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_furniture.object', {
#             'object': obj
#         })

