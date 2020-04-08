from odoo import models, fields

class ThingsHDC1080Celsius(models.Model):
    _name = 'things.data.hdc1080.celsius'
    _inherit = ['things.data.celsius']

    # every thing sends and/or receives data
    # through one and only one gate
    sensor_id = fields.Many2one('things.hdc1080',
                string='T & HR Sensor HDC1080',
                required = True)

    
class ThingsHDC1080(models.Model):
    _inherit = 'things.hdc1080'
 
    # Naming convention: 'thing_' + thingType + '_ids'
    # in order to easy reuse the main.py from controller folder
    # in this case: thingType = 'HDC1080' 
    temp_celsius_ids = fields.One2many(  
        'things.data.hdc1080.celsius',
        'sensor_id',
        string='Temp[°C]')
    

