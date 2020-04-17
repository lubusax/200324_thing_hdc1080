from odoo import http

class DataStreamHDC1080(http.Controller):


    @http.route('/things/data/incoming/<routeFrom>',
            type = 'json',
            auth ='public', csrf=False)    
    def messageFromThing(self, routeFrom, **kwargs):
        ThingModel = http.request.env['things.hdc1080']
        response = {
            'route known'       :   'false',
            'error'             :   'none'
        }
        
        thingSending = ThingModel.sudo().search(
            [('route_from', '=', routeFrom)])

        if thingSending:
            response = {'route known': 'true'}

            newTemperatureCelsius = float(kwargs.get('temperature celsius')) or None
            newRelativeHumidity = float(kwargs.get('relative humidity')) or None
            newBatteryLevel = float(kwargs.get('battery level')) or None
            response = self.storeData(
                            newTemperatureCelsius,
                            newRelativeHumidity,
                            newBatteryLevel,
                            thingSending,
                            response)

            #thingSending.sudo().prepareDataForCharts() 
            # better not, it slows the process too much

        else:
            response = {'error': 'unknown route'}
            
        return response

    def storeData(self,
        newTemperatureCelsius,
        newRelativeHumidity,
        newBatteryLevel,
        thingSending,
        response):

        newPoint = {
            'temperature_celsius'   : newTemperatureCelsius,
            'relative_humidity'     : newRelativeHumidity,
            'battery_level'         : newBatteryLevel
            }
        
        thingSending.write({
            'data_ids' : [(0,0,newPoint)]
            })

        thingSendingDict = thingSending.sudo().read()[0]

        print('thingSendingDict :', thingSendingDict)


        response['error']               = 'none'

        return response

        