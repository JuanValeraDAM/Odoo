from odoo import fields, models, api


class Modelo(models.Model):
    _name = 'ambulancias.modelo'
    _description = 'Modelos'

    name = fields.Char(string="Nombre", required=True)

    marca_id= fields.Many2one(comodel_name="ambulancias.marca", string="Marca")

    _sql_constraints = [
        ('name_marca_unicos','unique(marca_id, name)','La combinación entre nombre y marca debe ser única')
    ]