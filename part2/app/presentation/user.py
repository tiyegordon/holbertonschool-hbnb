#Import/Setup

from flask_restx import Namespace, Resource, fileds
from app.services.facade import Facade

api = Ma,espace ('user', description = ' User operations')
facade = Facade()

# Model Definition  = mandotory inputs - first name, last name, and email
user_model = api.model ('User',
                       {
                           'first_name': fields.String (required=True),
                           'last_name': fields.String(required=True),
                           'email': fields.String(required=True),
                           })
#Endpoints directed to resource class so any thing that htis the path goes to this class

@api.route('/')
class UserList(Resource):
    def get(self):          # When a GET request comes in, return all users
    def post(self):        # When a POST request comes in, create a new user

@api.route('/<id>')
class UserResource(Resource):
    def get(self):          # When a GET request comes in, return the one specific user
    def put(self):          # When a PUT request comes in udpate the one specific user

#API Structure

- namespace: 'user'
- model fields: first_name, last_name, email
- endpoints:
    GET /api/v1/user  #return all users
    POST /api/v1/user #create new user
    GET /api/v1/user/<id> #return one user
    PUT /api/v1/user/<id> #update one user
