from odoo import http
from odoo.addons.things.controllers.main import ThingsGate

class ThingsGateExtended(ThingsGate):

    @http.route()    
    def messageFromGate(self, routeFrom, **kwargs):
        response = super().messageFromGate(routeFrom, **kwargs)
        print('FROM HDC1080 - gateSending is ', response)
        print (' this is from HDC1080 - something came from', routeFrom)
        return {'message': 'thank you from HDC1080'}

