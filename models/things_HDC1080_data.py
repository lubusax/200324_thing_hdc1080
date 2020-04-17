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
    
    chartTemperature = fields.Text(
        string='Plotly Chart Temperature',
        #compute='prepareDataForCharts',
        )
    chartHumidity = fields.Text(
        string='Plotly Chart Humidity',
        #compute='prepareDataForCharts',
        )
    chartBattery = fields.Text(
        string='Plotly Chart Battery',
        #compute='prepareDataForCharts',
        )

    def prepareDataForCharts(self):
        time = []
        temperature = []
        humidity = []
        battery = []

        for id in self.data_ids:
            time.append(id.create_date)
            temperature.append(id.temperature_celsius)
            humidity.append(id.relative_humidity)
            battery.append(id.battery_level)

        dataTemperature = [{'x': time, 'y': temperature}]
        dataHumidity    = [{'x': time, 'y': humidity}]
        dataBattery     = [{'x': time, 'y': battery}]

        layoutTemperature = go.Layout(
            title=self.name + '- Temperature Chart',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Temperature [°C]')
            )

        layoutHumidity = go.Layout(
            title=self.name + '- Relative Humidity Chart',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Rel. Humidity [%]')
            )
        
        layoutBattery = go.Layout(
            title=self.name + '- Battery Level Chart',
            xaxis=dict(title='Time'),
            yaxis=dict(title='Voltage [V]')
            )

        self.chartTemperature = plotly.offline.plot(
            dict(data=dataTemperature, layout=layoutTemperature),
            include_plotlyjs=False,
            output_type='div')
        
        self.chartHumidity = plotly.offline.plot(
            dict(data=dataHumidity, layout=layoutHumidity),
            include_plotlyjs=False,
            output_type='div')

        self.chartBattery = plotly.offline.plot(
            dict(data=dataBattery, layout=layoutBattery),
            include_plotlyjs=False,
            output_type='div')

        return True

