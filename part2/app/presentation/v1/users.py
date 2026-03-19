from flask_restx import Namespace, Resource, fields
from app.blayer.facade import Facade

api = Namespace('users', description = 'User operations')

facade = Facade()

user_model = api.model ('Iser", {
                        'first_name': fields.String(
                        required=True,
                        description='First name of the user'
