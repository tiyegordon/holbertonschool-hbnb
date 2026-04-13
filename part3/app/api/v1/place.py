from flask_restx import Namespace, Resource, fields # Imports the tools to build/define API endpoints
from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('place', description = 'Place operations') #Creates a namespace grouping all place related endpoints together under one path

# Get facade from app context
def get_facade():
    return current_app.facade

#Converts place profile in JSON for API
place_model = api.model ('Place', 
    {
    'id': fields.String(readOnly=True, description='The place unique identifier'),
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude coordinate'),
    'longitude': fields.Float(required=True, description='Longitude coordinate'),
    'owner_id': fields.String(required=True, description='User ID of the owner'),
    'amenities': fields.List(fields.String, description='List of amenity IDs'),
    'reviews': fields.List(fields.String, description='List of review IDs'),
    })

@api.route('/')
class PlaceList(Resource):
    @api.doc('get_places')
    @api.marshal_list_with(place_model)
    def get(self):
        '''Get a list of all places'''
        return get_facade().get_all_places()

    @api.expect(place_model)
    @api.marshal_with(place_model, code='201')
    @jwt_required()
    def post(self):
        '''Create a new place'''
        current_user_id = get_jwt_identity()
        place_data = api.payload
        place_data['owner_id'] = current_user_id
        return get_facade().create_place(place_data), 201

@api.route('/<string:place_id>')
@api.param('place_id', 'The place identifier')
@api.response(404, 'Place not found')
class PlaceResource(Resource):
    @api.doc('get_place')
    @jwt_required()
    def get(self, place_id):
        '''Get a place given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        place = get_facade().get_place(place_id)
        if not place:
            return {'message': 'Place not found'}, 404
        # Check ownership or admin
        if not current_user or (place.owner_id != current_user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        return api.marshal(place, place_model)

    @api.expect(place_model)
    @jwt_required()
    def put(self, place_id):
        '''Update a place given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        place = get_facade().get_place(place_id)
        if not place:
            return {'message': 'Place not found'}, 404
        # Check ownership or admin
        if not current_user or (place.owner_id != current_user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        place_data = api.payload
        # Prevent non-admins from changing owner_id
        if not current_user.is_admin and 'owner_id' in place_data:
            del place_data['owner_id']
        updated_place = get_facade().update_place(place_id, place_data)
        if not updated_place:
            return {'message': 'Place not found'}, 404
        return api.marshal(updated_place, place_model)

    @api.response(204, 'Place deleted')
    @jwt_required()
    def delete(self, place_id):
        '''Delete a place given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        place = get_facade().get_place(place_id)
        if not place:
            return {'message': 'Place not found'}, 404
        if not current_user or (place.owner_id != current_user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        deleted = get_facade().delete_place(place_id)
        if not deleted:
            return {'message': 'Place not found'}, 404
        return '', 204
