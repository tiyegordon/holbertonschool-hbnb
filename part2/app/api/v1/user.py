from flask_restx importNamespace, Resource, fields # Imports the tools to build/define API endpoints
from app.blayer.facade import Facade #Import facade that connects API to business logic layer (blayer)

api = Namespace('user', description = 'User operations') #Creates a namespace grouping all user related enpoitns together under one path00

facade = Facade() #Create a shared facade instance so all endpoints in this file can talk to business logic layer

#Converts user profile in JSON for API
user_model = api.model ('User', 
    {
    'first_name': fields.String(required=True, description='First name of the user'), # First name is mandatory, can't be left blank
    'last_name': fields.String(required=True, description='Last name of the user'),# Last name is mandatory, cant be left blank
    'email': fields.String(required=True, description='Email address of the user'), # Email is mandatory, can't be blank
    })



