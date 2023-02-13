from odoo import fields, models, api


class CDU(models.Model):
    _name = 'milibro.cdu'
    _description = 'Description'

    name = fields.Char(string="Código")
    description = fields.Char(string="Descripción")

    @api.model
    def name_get(self):
        lista = []
        for r in self:
            lista.append((r.id, r.name + "-" + r.description))
        return lista
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args: []
        domain = args + ['|', ('name', operator, name), ('description', operator, name)]
        return self.search(domain, limit=limit).name_get()
