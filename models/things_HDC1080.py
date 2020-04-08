from odoo import models, fields

class ThingsHDC1080(models.Model):
    _name = 'things.hdc1080'
    _inherit = ['things.basis']
    
    name = fields.Char(
            string= 'Temperature and Relative '+  \
            'Humidity Sensor Identifier')

    # every thing sends and/or receives data
    # through one and only one gate
    gate_id = fields.Many2one('things.gate',
                string='Gate',
                required = True)

    
class ThingsGate(models.Model):
    _inherit = 'things.gate'
 
    # Naming convention: 'thing_' + thingType + '_ids'
    # in order to easy reuse the main.py from controller folder
    # in this case: thingType = 'HDC1080' 
    thing_HDC1080_ids = fields.One2many(  
        'things.hdc1080',
        'gate_id', string='T & HR Sensor HDC1080')
    

