from flask_restx import Namespace, Resource, fields
from app.services.facade import Facade

api = Namespace ('place', description='Place operations')
facade = Facade()

# Model Definition  = mandotory inputs - first name, last name, and email
place_model = api.model('Place',
                        {
                            'title': fields.String(required=True),
                            'description': fields.String(required=True)
                            'price': fields.Float(required=True),
                            'latitudde': fields.Float(required=True),
                            'owner_id': fields.String(required=True),

#Endpoints directed to resource class so any thing that htis the path goes to this class

@api.route('/')
class UserList(Resource):
    def get(self):          # When a GET request comes in, return all users
    def post(self):        # When a POST request comes in, create a new user

@api.route('/<id>')
class UserResource(Resource):
    def get(self):          # When a GET request comes in, return the one specific user
    def put(self):          # When a PUT request comes in udpate the one specific user


