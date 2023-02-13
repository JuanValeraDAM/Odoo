from odoo import fields, models, api


class Marca(models.Model):
    _name = 'ambulancias.marca'
    _description = 'Marcas'

    name = fields.Char(string="Nombre", required=True)

    _sql_constraints = [
        ('name_unico','unique(name)','El nombre debe ser único')
    ]
