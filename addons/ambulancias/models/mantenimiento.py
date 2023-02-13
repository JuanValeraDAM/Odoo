from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import datetime


class Mantenimiento(models.Model):
    _name = 'ambulancias.mantenimiento'
    _description = 'Mantenimientos'

    km = fields.Integer(string="Kilómetros", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    importe_mantenimiento = fields.Float(string="Total", compute="_calcular_importe_mantenimiento")

    vehiculo_id = fields.Many2one(comodel_name="ambulancias.vehiculo", string="Vehículo")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Taller",domain="[('es_taller','=','True')]")
    mantenimiento_linea_ids = fields.One2many(comodel_name="ambulancias.mantenimiento_linea", inverse_name="mantenimiento_id")

    @api.onchange("fecha")
    def _comprobar_fecha(self):
        res = {}
        for r in self:
            if r.fecha:
                if r.fecha > datetime.date.today():
                    res['warning'] = {'title': 'Peligrosísimo',
                                      'message': 'La fecha no puede ser mayor a la fecha actual'}

        return res

    @api.constrains("fecha")
    def _comprobar_fecha_constrains(self):
        for r in self:
            if r.fecha > datetime.date.today():
                raise ValidationError("BBDD Constrains: La fecha no puede ser mayor a la fecha actual")