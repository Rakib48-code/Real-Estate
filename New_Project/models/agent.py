from odoo import api, fields, models

class Agent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Agent Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    property_ids = fields.One2many( 'real.estate.property','agent_id',string='Properties')
