from odoo import http
from odoo.addons.things.controllers.main import ThingsGate

class ThingsGateExtended(ThingsGate):

    @http.route()    
    def messageFromGate(self, routeFrom, **kwargs):
        response = super().messageFromGate(routeFrom, **kwargs)
        print('response HDC1080 ', response)
        routeKnown = response['route known']
        if routeKnown == 'true':
            thingType= kwargs.get('thing type')
            if thingType== 'HDC1080':
                print('FROM HDC1080 - gateSendingDict is ', response)
                print (' this is from HDC1080 - something came from', routeFrom)
                response['thing type created'] = 'HDC1080'
        return response

