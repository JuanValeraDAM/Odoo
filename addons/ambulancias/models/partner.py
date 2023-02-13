from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    es_taller = fields.Boolean(string="Taller")
    es_gasolinera = fields.Boolean(string="Gasolinera")

