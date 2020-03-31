from odoo import models, fields
from odoo.exceptions import UserError

class HDC1080CreateWizard(models.TransientModel):
    _name = 'hdc1080.create.wizard'
    _description = 'description'
    
    name = fields.Char(
        string= 'Temperature and Relative '+  \
                'Humidity Sensor Name')
    
    gate_id = fields.Many2one('things.gate',
            string='Gate',
            required = True)

    def create_new_connection(self):
        self.ensure_one()
        
        new_thing = {
                'name' : self.name,
                }

        self.gate_id.write({
                'thing_hdc1080_ids' : [(0,0,new_thing)]
                })
