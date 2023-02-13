from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Libro(models.Model):
    _name = 'milibro.libro'
    _description = 'milibro.libro'

    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Resumen", required=True)
    isbn = fields.Char(string="ISBN")

    # Relaciones
    categoria_ids = fields.Many2many(comodel_name="milibro.categoria", string="categoria")
    autor_id = fields.Many2one(comodel_name="milibro.autor", string="Autor")
    editorial_id = fields.Many2one(comodel_name="milibro.editorial", string="Editorial")
    ejemplar_ids= fields.One2many(comodel_name="milibro.ejemplar", inverse_name="libro_id")

    num_paginas = fields.Integer(string="Número de páginas")

    cdu_id = fields.Many2one(comodel_name="milibro.cdu", string="CDU")
    tejuelo_id = fields.Char(string="Tejuelo")

    imagen = fields.Image(string="Imagen", max_width=425, max_height=640)

    num_ejemplares = fields.Integer(compute="_calcular_ejemplares", string="Libros")
    num_ejemplares_disponibles = fields.Integer(compute="_calcular_ejemplares", string="Disponibles")


    # _sql_constraints = [
    #     ('isbn_unico', 'unique(isbn)', 'Pero tonto cuidaooo TOONMTO')
    # ]

    @api.onchange("num_paginas")
    def _calcular_num_paginas(self):
        res = {}
        for r in self:
            if r.num_paginas < 0:
                res['warning'] = {'title': 'Ojo cuidado', 'message': 'CUIDAAAAAO'}
        return res

    @api.constrains("num_paginas")
    def _calcular_num_paginas_constrains(self):
        for r in self:
            if r.num_paginas < 0:
                raise ValidationError("CHACHO CUIDAAAAAOOOO")

    @api.onchange("cdu_id", "autor_id", "name")
    def _calcular_tejuelo(self):
        for r in self:
           if r.cdu_id and r.autor_id and r.name:
               r.tejuelo_id=str(f'{r.cdu_id.name}-{r.name.upper()[:3]}-{r.autor_id.apellidos.lower()[:3]}')

    @api.depends("ejemplar_ids")
    def _calcular_ejemplares(self):
        for r in self:
            ejemplares = self.env['milibro.ejemplar'].search([('libro_id', '=', r.id)])
            r.num_ejemplares = len(ejemplares)
            r.num_ejemplares_disponibles = len(ejemplares.filtered(lambda c: c.situacion))

