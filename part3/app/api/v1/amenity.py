from flask_restx import Namespace, Resource, fields # Imports the tools to build/define API endpoints
from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('amenity', description = 'Amenity operations') #Creates a namespace grouping all amenity related endpoints together under one path

# Get facade from app context
def get_facade():
    return current_app.facade

#Converts amenity profile in JSON for API
amenity_model = api.model ('Amenity', 
    {
    'id': fields.String(readOnly=True, description='The amenity unique identifier'),
    'name': fields.String(required=True, description='Name of the amenity'), # Name is mandatory, can't be left blank
    })

@api.route('/')
class AmenityList(Resource):
    @api.doc('get_amenities', security='Bearer Auth')
    @api.marshal_list_with(amenity_model)
    def get(self):
        '''Get a list of all amenities'''
        return get_facade().get_all_amenities()

    @api.expect(amenity_model)
    @jwt_required()
    def post(self):
        '''Create a new amenity (admin only)'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        if not current_user or not current_user.is_admin:
            return {'message': 'Admin access required'}, 403
        amenity_data = api.payload
        amenity = get_facade().create_amenity(amenity_data)
        return api.marshal(amenity, amenity_model), 201

@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'The amenity identifier')
@api.response(404, 'Amenity not found')
class AmenityResource(Resource):
    @api.doc('get_amenity')
    @api.marshal_with(amenity_model)
    @jwt_required()
    def get(self, amenity_id):
        '''Get an amenity given its identifier'''
        return get_facade().get_amenity(amenity_id)

    @api.expect(amenity_model)
    @jwt_required()
    def put(self, amenity_id):
        '''Update an amenity given its identifier (admin only)'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        if not current_user or not current_user.is_admin:
            return {'message': 'Admin access required'}, 403
        amenity_data = api.payload
        updated_amenity = get_facade().update_amenity(amenity_id, amenity_data)
        if not updated_amenity:
            return {'message': 'Amenity not found'}, 404
        return api.marshal(updated_amenity, amenity_model)

    @api.response(204, 'Amenity deleted')
    @jwt_required()
    def delete(self, amenity_id):
        '''Delete an amenity given its identifier (admin only)'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        if not current_user or not current_user.is_admin:
            return {'message': 'Admin access required'}, 403
        deleted = get_facade().delete_amenity(amenity_id)
        if not deleted:
            return {'message': 'Amenity not found'}, 404
        return '', 204
