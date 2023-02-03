from odoo import fields, models, api
#TODO: El cdu dice que ValueError: dictionary update sequence element #0 has length 9; 2 is required

class ModelName(models.Model):
    _name = 'milibro.cdu'
    _description = 'milibro.cdu'

    name = fields.Char(label= "código")
    description = fields.Char(label= "Descripción")

    @api.model
    def name_get(self):
        lista = []
        for r in self:
            lista.append((r.id,r.name+"-"+r.description))
        return lista

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', ('name', operator, name), ('description', operator, name)]
        return self.search(domain, limit=limit).name_get()