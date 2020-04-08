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

            newTemperatureCelsius = kwargs.get('temperature celsius') or None
            newRelativeHumidity = kwargs.get('relative humidity') or None
            response = self.storeTemperatureCelsiusPoint(
                            newTemperatureCelsius,
                            thingSending,
                            response)

        else:
            response = {'error': 'unknown route'}
            
        return response

    def storeTemperatureCelsiusPoint(self,
        newTemperatureCelsius,
        thingSending,
        response):

        newValue = float(newTemperatureCelsius)

        newPoint = {
            'temperature_celsius' : newValue,
            }
        
        thingSending.write({
            'temp_celsius_ids' : [(0,0,newPoint)]
            })

        thingSendingDict = thingSending.sudo().read()[0]

        print('thingSendingDict :', thingSendingDict)


        response['error']               = 'none'

        return response

        