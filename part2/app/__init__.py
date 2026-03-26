from flask import Flask # framework that runs the web server
from flask_restx import Api #adds REST API features/creates a free Swager UI page for testing
from config import config #config settings (debug mode and secret key) from config.py

def create_app(config_name='default'): 


    app = Flask(__name__) #creats flask app

    app.config.from_object(config[config_name]) #loads settings into 

    api = Api(app, version ='1.0', title = 'HBnB API', description='HBnB RESTful API')

    from app.api.v1.user import api as users_ns  #loads user endpoint
    from app.api.v1.amenity import api as amenities_ns #loads amentiy endpoints
    from app.api.v1.place import api as places_ns #loads place endpoints
    from app.api.v1.review import api as reviews_ns #loads review endpoints

#URLs for each group of endpoints/where endpoints live and communicates location to flask

    api.add_namespace(users_ns, path='api/v1/user')
    api.add_namespace(amenities_ns, path='api/v1/amenitiy')
    api.add_namespace(places_ns, path='api/v1/place')
    api.add_namespace(reviews_ns, path='api/v1/review')
