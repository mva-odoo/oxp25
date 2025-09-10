from odoo import models, fields


class Furniture(models.Model):
    _name = 'furniture'
    _description = 'furniture'

    name = fields.Char(required=True)
    description = fields.Html()
    image = fields.Image(string="Bank Logo")
