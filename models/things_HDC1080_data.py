from odoo import models, fields
import plotly
# import datetime
import plotly.graph_objects as go

class ThingsHDC1080Data(models.Model):
    _name = 'things.data.hdc1080'
    _description = 'description'
    
    temperature_celsius = fields.Float('T[°C]')
    relative_humidity =  fields.Float('RH[%]')
    battery_level =  fields.Float('Voltage[V]')

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
    data_ids = fields.One2many(  
        'things.data.hdc1080',
        'sensor_id',
        string='data record')
    

    plotlyChartTemperature = fields.Text(
        string='Plotly Chart Temperature',
        compute='prepareDataForChart',
        )

    def prepareDataForChart(self):
        x=[]
        y=[]
        for id in self.data_ids:
            x.append(id.create_date)
            y.append(id.temperature_celsius)
        data = [{'x': x, 'y': y}]

        print(data)

        layout = go.Layout(
            title=self.name,
            xaxis=dict(title='Time'),
            yaxis=dict(title='Temperature [°C]')
            )

        self.plotlyChartTemperature = plotly.offline.plot(
            dict(data=data, layout=layout),
            include_plotlyjs=False,
            output_type='div')
