from odoo import models, fields

class ThingsThing(models.Model):
    _inherit = 'base.thing'
    _name = 'things.thing.hdc1080'

    # every thing sends and/or receives data
    # through one and only one gate
    gate_id = fields.Many2one('things.gate',
                string='Gate',
                required = True)
    
class ThingsGate(models.Model):
    _inherit = 'things.gate'

    thing_hdc1080_ids = fields.One2many(
        'things.thing.hdc1080',
        'gate_id', string='T & HR Sensor HDC1080')
    

