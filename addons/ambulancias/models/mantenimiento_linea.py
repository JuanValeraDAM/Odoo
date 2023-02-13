from odoo import fields, models, api


class MantenimientoLinea(models.Model):
    _name = 'ambulancias.mantenimiento_linea'
    _description = 'Líneas de mantenimiento'

    name = fields.Char(string="Descripción", required=True)
    importe = fields.Float(string="Importe", required=True)

    mantenimiento_id= fields.Many2one(comodel_name="ambulancias.mantenimiento", string="Línea de mantenimiento")