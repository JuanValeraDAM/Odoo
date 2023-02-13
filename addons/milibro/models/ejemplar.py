from odoo import fields, models, api


class Ejemplar(models.Model):
    _name = 'milibro.ejemplar'
    _description = 'milibro.ejemplar'

    name = fields.Char(string="Código", compute="_calcular_name")
    situacion = fields.Boolean(string="Disponible", default=True)
    estado = fields.Selection([('1', 'Bueno'), ('2', 'Regular'), ('3', 'Malo')], required=True,
                              string="Estado de conservación", default='1')

    libro_id = fields.Many2one(comodel_name="milibro.libro", string="Libro")

    @api.depends("create_date")
    def _calcular_name(self):
        for r in self:
            r.name = str(r.id).zfill(13)
