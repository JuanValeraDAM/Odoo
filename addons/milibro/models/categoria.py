from odoo import fields, models, api


class Categoria(models.Model):
    _name = 'milibro.categoria'
    _description = 'milibro.categoria'

    name = fields.Char(string="Nombre", required=True)
    libro_ids = fields.Many2many(comodel_name="milibro.libro", string="libro", required=True)
