from odoo import api,fields, models

class Property(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Property Name', required=True)
    location = fields.Char(string='Location')
    price = fields.Float(string='Price')
    property_type = fields.Selection([
        ('sale','Sale'),
        ('rent','Rent')
    ], string='Property Type', default='sale')
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('available','Available'),
        ('sold','Sold'),
        ('rented','Rented')
    ], string='Status', default='available')
    agent_id = fields.Many2one('real.estate.agent',string='Agent')
    client_id = fields.Many2one('real.estate.client', string='Client')
