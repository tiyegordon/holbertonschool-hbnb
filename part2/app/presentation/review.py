#Import/Setup

from flask_restx import Namespace, Resource, fileds
from app.services.facade import Facade

api = Namespace ('review', description = 'REview operations')
facade = Facade()

# Model Definition  = mandotory inputs - first name, last name, and email
review_model = api.model ('Review',
                       {
                           'text': fields.String (required=True),
                           'rating': fields.String(required=True),
                           'place_id': fields.String(required=True),
                           'user_id': fields.String(required=True_),
                           })
#Endpoints directed to resource class so any thing that htis the path goes to this class

@api.route('/')
class ReviewList(Resource):
    def get(self):          # When a GET request comes in, return all reviews
    def post(self):        # When a POST request comes in, create a new review

@api.route('/<id>')
class REviewResource(Resource):
    def get(self):          # When a GET request comes in, return the one specific review
    def put(self):          # When a PUT request comes in udpate the one specific review

