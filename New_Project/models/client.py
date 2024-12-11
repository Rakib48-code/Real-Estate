from odoo import api, fields, models

class Client(models.Model):
    _name = 'real.estate.client'
    _description = 'Real Estate Client'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    property_ids = fields.One2many('real.estate.property', 'client_id' , string='Properties')