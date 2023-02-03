from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'milibro.ejemplar'
    _description = 'milibro.ejemplar'

    name = fields.Char(label="Código", compute="calcular_name")
    situacion=fields.Boolean(label="Disponible", default=True)
    estado=fields.Selection([('1','Bueno'),('2','Regular'),('3','Malo')],required=True, label="Estado de conservación")

  ##TODO: faltan las relaciones
    @api.depends("create_date")
    def calcular_name(self):
        for r in self:
            r.name=str(r.id).zfill(13)