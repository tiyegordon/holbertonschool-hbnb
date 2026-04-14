from flask import Flask # framework that runs the web server
from flask_restx import Api #adds REST API features/creates a free Swager UI page for testing
from config import config #config settings (debug mode and secret key) from config.py
from flask_cors import CORS

def create_app(config_name='default'): 
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    app.config['API_SPEC_OPTIONS'] = {
        'components': {
            'securitySchemes': {
                'bearerAuth': {
                    'type': 'http',
                    'scheme': 'bearer',
                    'bearerFormat': 'JWT'
                }
            }
        }
    }
    
    # Initialize extensions
    from app.extensions import db, jwt
    db.init_app(app)
    jwt.init_app(app)
    
    # Import models after db is initialized to avoid circular imports
    from app.blayer.user import User
    from app.blayer.review import Review
    from app.blayer.amenity import Amenity
    from app.blayer.place import Place
    from app.blayer.facade import Facade
    from app.persistence.sqlalchemy_repository import SQLAlchemyRepository
    
    # Create SQLAlchemy repositories
    user_repo = SQLAlchemyRepository(User)
    place_repo = SQLAlchemyRepository(Place)
    review_repo = SQLAlchemyRepository(Review)
    amenity_repo = SQLAlchemyRepository(Amenity)
    
    # Initialize repositories with db session
    user_repo.init_app(db)
    place_repo.init_app(db)
    review_repo.init_app(db)
    amenity_repo.init_app(db)

   # Create facade with SQLAlchemy repositories
    facade = Facade(user_repo=user_repo, place_repo=place_repo, review_repo=review_repo, amenity_repo=amenity_repo)
    
    # Make facade available globally (you might want to use a better pattern like app context)
    app.facade = facade
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Authorization settings for Swagger UI
    authorizations = {
         'Bearer Auth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Paste your JWT token (without 'Bearer ' prefix)"
        }
    }
    
    api = Api(app, 
              version='1.0', 
              title='HBnB API', 
              description='HBnB RESTful API',
              authorizations=authorizations,
              security='Bearer Auth')
    from app.api.v1.user import api as users_ns
    from app.api.v1.amenity import api as amenities_ns
    from app.api.v1.place import api as places_ns
    from app.api.v1.review import api as reviews_ns
    api.add_namespace(users_ns, path='/api/v1/user')
    api.add_namespace(amenities_ns, path='/api/v1/amenity')
    api.add_namespace(places_ns, path='/api/v1/place')
    api.add_namespace(reviews_ns, path='/api/v1/review')
    return app

