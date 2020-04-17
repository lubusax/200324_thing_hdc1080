from odoo import http
from odoo.addons.things.controllers.main import ThingsGate

class ThingsGateExtended(ThingsGate):

    @http.route()    
    def messageFromGate(self, routeFrom, **kwargs):
        moduleType = 'HDC1080' # this Variable is thing type dependent
        ThingModel = http.request.env['things.hdc1080']
                # this Model is thing type dependent

        response = super().messageFromGate(routeFrom, **kwargs)

        response = self.modifyResponse(response,
                ThingModel, moduleType, routeFrom, **kwargs)

        return response

    def modifyResponse(self, response,
                ThingModel, moduleType, routeFrom, **kwargs):

        routeKnown = response['gate route known']
        thingType= kwargs.get('thing type')
        thingIdentifier = kwargs.get('thing identifier')

                   
        if not thingIdentifier:
            response['error']   = 'Name must exist'            
        elif ThingModel.sudo().search(
                [('name', '=', thingIdentifier)]):
            response['error']   = 'Name must be unique'
        elif  routeKnown  == 'false':
            response['error']   = 'Given Gate Route unknown'
        elif thingType   == moduleType:

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

            thingCreated = ThingModel.sudo().search(
                [('name', '=', thingIdentifier)]).sudo().read()[0]

            response['route from']          = thingCreated['route_from']
            response['route to']            = thingCreated['route_to']           
            response['thing type created']  = moduleType
            response['error']               = 'none'

            #print('thing created :', thingCreated)
            # print('FROM ', moduleType)
            # print('\nGate Created Dict is ', gateSending.sudo().read()[0])
            print('\nResponse is ', response)
            # print ('\nSomething came from', routeFrom)

        return response

