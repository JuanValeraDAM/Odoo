import datetime
import re

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Prestamo(models.Model):
    _name = 'milibro.prestamo'
    _description = 'milibro.prestamo'

    name = fields.Char(string="Número de préstamo", compute="_calcular_num_prestamo")
    fecha_iniprestamo = fields.Date(default=fields.Date.today, required=True, string="Fecha de préstamo")
    fecha_devolucion = fields.Date(string="Fecha de devolución")
    fecha_finprestamo = fields.Date(string="Fecha fin de préstamo", store=True, compute="_calcular_fecha_finprestamo")
    estado = fields.Selection([('1', 'Creando'), ('2', 'Prestado'), ('3', 'Devuelto')], required=True, default='1')

    # Relaciones

    libro_id = fields.Many2one(comodel_name="milibro.libro", string="Libro")
    autor_id = fields.Many2one(comodel_name="milibro.autor", string="Autor")
    ejemplar_id = fields.Many2one(comodel_name="milibro.ejemplar", string="Ejemplar", required=True)
    usuario = fields.Many2one(comodel_name="res.partner", required=True, string="Usuario")

    @api.depends("create_date")
    def _calcular_num_prestamo(self):
        for r in self:
            date_str = str(r.create_date)
            date_num = re.sub(r'\D', '', date_str)
            r.name = date_num

    @api.depends("fecha_iniprestamo")
    def _calcular_fecha_finprestamo(self):
        for r in self:
            fecha_finprestamo = r.fecha_iniprestamo + datetime.timedelta(days=15)
            if fecha_finprestamo.weekday() >= 5:
                fecha_finprestamo = fecha_finprestamo + datetime.timedelta(days=(7 - fecha_finprestamo.weekday()))
            r.fecha_finprestamo = fecha_finprestamo

    @api.onchange("fecha_iniprestamo")
    def _calcular_fecha_iniprestamo(self):
        fechaHoy = fields.Date().today()
        res = {}
        for r in self:
            if r.fecha_iniprestamo > fechaHoy:
                res['warning'] = {'title': 'Ojo cuidado', 'message': 'CUIDAAAAAO'}
                r.fecha_iniprestamo = fechaHoy
        return res

    @api.constrains("fecha_iniprestamo")
    def _calcular_fecha_iniprestamo_constrains(self):
        fechaHoy = fields.Date().today()
        for r in self:
            if r.fecha_iniprestamo > fechaHoy:
                raise ValidationError("TAS TONTO O QUE")


    @api.onchange("autor_id")
    def _cambio_autor(self):
        if self.autor_id.id is not self.libro_id.autor_id.id:
            self.libro_id = False

    @api.onchange("libro_id")
    def _cambio_libro(self):
        if self.libro_id.id is not self.ejemplar_id.libro_id.id:
            self.ejemplar_id = False

    def create(self):
        self.estado='2'
        self.ejemplar_id.estado = False
