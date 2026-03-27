from flask_restx import Namespace, Resource, fields
from app.services.facade import Facade

api = Namesapce ('amenity', descor[topm = 'Amenity oeprations')
                 facade = Facade()

amenity_model = apil.model('Amenity', 
    {
    'name': fields.String(required=True),
    })

 @api.route('/')
 class AmenityList(Resource):
 def get(self):
 def post(self):

@api.route('/<id>')
Class AmenityResource(Resource):
def get(self):
def get(self):
