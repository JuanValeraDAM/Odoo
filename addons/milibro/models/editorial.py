from odoo import fields, models, api


class Editorial(models.Model):
    _name = 'milibro.editorial'
    _description = 'milibro.editorial'

    name = fields.Char(string="Nombre", required=True)
    direccion=fields.Char(string="Dirección")
    poblacion=fields.Char(string="Población")

    cantidad_libros=fields.Integer(compute="_num_libros")

    # Relaciones
    libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="editorial_id")

    @api.depends("libro_ids")
    def _num_libros(self):
        for r in self:
            r.cantidad_libros=len(r.libro_ids)