from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import datetime


class Repostaje(models.Model):
    _name = 'ambulancias.repostaje'
    _description = 'Repostajes'

    km = fields.Integer(string="Kilómetros", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    litros = fields.Float(string="Litros", required=True)
    importe_repostado = fields.Float(string="Importe", required=True)
    consumo_100 = fields.Float(string="Consumo a 100km", compute="_calcular_consumo")

    vehiculo_id = fields.Many2one(comodel_name="ambulancias.vehiculo", string="Vehículo")
    partner_id = fields.Many2one(comodel_name="res.partner",string="Gasolinera",domain="[('es_gasolinera','=','True')]")


    @api.onchange("fecha")
    def _comprobar_fecha(self):
        res = {}
        for r in self:
            if r.fecha:
                if r.fecha > datetime.date.today():
                    res['warning'] = {'title': 'Cuidadísimo',
                                      'message': 'La fecha no puede ser mayor a la fecha actual'}

        return res

    @api.constrains("fecha")
    def _comprobar_fecha_constrains(self):
        for r in self:
            if r.fecha > datetime.date.today():
                raise ValidationError("BBDD Constrains: La fecha no puede ser mayor a la fecha actual")