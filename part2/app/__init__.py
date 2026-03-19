from flask import Flask # framework that runs the web server
from flask_restx import Api #adds REST API features/creates a free Swager UI page for testing
from config import config #config settings (debug mode and secret key) from config.py

def create_app(config_name='default'): 

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    api = Api(app, version ='1.0', title = 'HBnB API', description='HBnB RESful API')

    from app.api.v1.user import api as users_ns
    from app.api.v1.amenity import api as amenities_ns
    from app.api.v1.place import api as places_ns
    from app.api.v1.review import api as reviews_ns

    api.add_namespace(users_ns, path='api/v1/user')
    api.add_namespace(amenities_ns, path='api/v1/amenitiy')
    api.add_namespace(places_ns, path='api/v1/place')
    api.add_namespace(reviews_ns, path='api/v1/review')
