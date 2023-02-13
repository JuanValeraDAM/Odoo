from odoo import fields, models, api


class Autor(models.Model):
    _name = 'milibro.autor'
    _description = 'milibro.autor'

    name = fields.Char(compute="_nombre_completo")
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    cantidad_libros_escritos = fields.Integer(compute="_num_libros_escritos")

    # Relaciones
    libro_ids = fields.One2many(comodel_name="milibro.libro", inverse_name="autor_id")

    @api.depends("libro_ids")
    def _num_libros_escritos(self):
        for r in self:
            r.cantidad_libros_escritos = len(r.libro_ids)

    @api.depends("nombre", "apellidos")
    def _nombre_completo(self):
        for r in self:
            r.name = str(f'{r.apellidos}, {r.nombre}')
