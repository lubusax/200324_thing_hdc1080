from odoo import http
from odoo.addons.things.controllers.main import ThingsGate

class ThingsGateExtended(ThingsGate):

    @http.route()    
    def messageFromGate(self, routeFrom, **kwargs):
        moduleType = 'HDC1080' # only this Variable should be modified

        response = super().messageFromGate(routeFrom, **kwargs)

        response = self.modifyResponse(response, moduleType, routeFrom, **kwargs)

        return response

    def modifyResponse(self, response, moduleType, routeFrom, **kwargs):

        routeKnown = response['route known']
        thingType= kwargs.get('thing type')

        if routeKnown == 'true' and thingType== moduleType:
            thingIdentifier = kwargs.get('thing identifier') or 'none'

            new_thing = {
                'name' : thingIdentifier,
                }
            GatesModel = http.request.env['things.gate']
            gateSending = GatesModel.sudo().search(
                [('route_from', '=', routeFrom)])
            idsField = 'thing_' + thingType + '_ids'
            gateSending.write({
                idsField : [(0,0,new_thing)]
                })
            
            response['thing type created'] = moduleType

            # print('FROM ', moduleType)
            # print('\nGate Created Dict is ', gateSending.sudo().read()[0])
            # print('\nResponse is ', response)
            # print ('\nSomething came from', routeFrom)

        return response

