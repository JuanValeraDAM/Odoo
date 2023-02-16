import re

from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import datetime


class Vehiculo(models.Model):
    _name = 'ambulancias.vehiculo'
    _description = 'Vehículos'
    _inherit = 'image.mixin'

    borrar=fields.Char(string="Esto hay que borrarlo")

    name = fields.Char(string="Matrícula", unique=True, required=True)
    fecha_adquisicion = fields.Date(string="Fecha de adquisición", required=True)
    fecha_baja = fields.Date(string="Fecha de baja")
    num_bastidor = fields.Char(string="Número de bastidor", unique=True, required=True)
    fecha_proximo_mantenimiento = fields.Date(string="Fecha del próximo mantenimiento")
    precio_adquisicion = fields.Float(string="Precio de adquisición")
    total_repostajes = fields.Float(string="Total repostajes", compute="_calcular_total_repostajes")
    total_mantenimientos = fields.Float(string="Total mantenimientos", compute="_calcular_total_mantenimientos")
    observaciones = fields.Text(string="Observaciones")
    estado = fields.Selection([('0', 'En uso'), ('1', 'Vendido'), ('2', 'Baja')], default='0')

    marca_id = fields.Many2one(comodel_name="ambulancias.marca", string="Marca")
    modelo_id = fields.Many2one(comodel_name="ambulancias.modelo", string="Modelo")
    repostaje_ids = fields.One2many(comodel_name="ambulancias.repostaje", inverse_name="vehiculo_id", string="Vehículo")
    mantenimiento_ids = fields.One2many(comodel_name="ambulancias.mantenimiento", inverse_name="vehiculo_id",
                                        string="Vehículo")

    _sql_constraints = [
        ('name_unico', 'unique(name)', 'La matrícula debe ser única'),
        ('num_bastidor_unico', 'unique(num_bastidor)', 'El número de bastidor debe ser único')
    ]

    @api.onchange("name")
    def _comprobar_nombre(self):
        res = {}
        for r in self:
            regex = re.compile(r"\d{4}-[A-Z]{3}")
            m = regex.match(str(r.name))
            if not m:
                res['warning'] = {'title': 'Peligro',
                                  'message': 'La matrícula debe tener 4 números un guión y 3 letras'}
        return res;

    @api.constrains("name")
    def _comprobar_nombre_constrains(self):
        for r in self:
            regex = re.compile(r"\d{4}-[A-Z]{3}")
            m = regex.match(str(r.name))
            if not m:
                raise ValidationError("BBDD Constrains: La matrícula debe tener 4 números un guion y 3 letras")

    @api.onchange("fecha_adquisicion")
    def _comprobar_fecha_adquisicion(self):
        res = {}
        for r in self:
            if r.fecha_adquisicion:
                if r.fecha_adquisicion > datetime.date.today():
                    res['warning'] = {'title': 'Peligroso',
                                      'message': 'La fecha de adquisición no puede ser mayor a la fecha actual'}

        return res

    @api.constrains("fecha_adquisicion")
    def _comprobar_fecha_adquisicion_constrains(self):
        for r in self:
            if r.fecha_adquisicion > datetime.date.today():
                raise ValidationError("BBDD Constrains: La fecha de adquisición no puede ser mayor a la fecha actual")

    @api.onchange("fecha_baja")
    def _comprobar_fecha_baja(self):
        res = {}
        for r in self:
            if r.fecha_baja:
                if r.fecha_baja > datetime.date.today():
                    res['warning'] = {'title': 'Cuidado',
                                      'message': 'La fecha de baja no puede ser mayor a la fecha actual'}

        return res

    @api.constrains("fecha_baja")
    def _comprobar_fecha_baja_constrains(self):
        for r in self:
            if r.fecha_baja > datetime.date.today():
                raise ValidationError("BBDD Constrains: La fecha de baja no puede ser mayor a la fecha actual")

    @api.onchange("fecha_proximo_mantenimiento")
    def _comprobar_fecha_proximo_mantenimiento(self):
        res = {}
        for r in self:
            if r.fecha_proximo_mantenimiento:
                if r.fecha_proximo_mantenimiento < datetime.date.today():
                    res['warning'] = {'title': 'Cuidadín',
                                      'message': 'La fecha del próximo mantenimiento no puede ser menor a la fecha '
                                                 'actual'}

        return res

    @api.constrains("fecha_proximo_mantenimiento")
    def _comprobar_fecha_proximo_mantenimiento_constrains(self):
        for r in self:
            if r.fecha_proximo_mantenimiento < datetime.date.today():
                raise ValidationError("BBDD Constrains: La fecha del próximo mantenimiento no puede ser menor a la "
                                      "fecha actual")
