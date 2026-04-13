from flask_restx import Namespace, Resource, fields # Imports the tools to build/define API endpoints
from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('review', description = 'Review operations') #Creates a namespace grouping all review related endpoints together under one path

# Get facade from app context
def get_facade():
    return current_app.facade

#Converts review profile in JSON for API
review_model = api.model ('Review', 
    {
    'id': fields.String(readOnly=True, description='The review unique identifier'),
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='Place ID'),
    'user_id': fields.String(required=True, description='User ID'),
    })

@api.route('/')
class ReviewList(Resource):
    @api.doc('get_reviews')
    @api.marshal_list_with(review_model)
    def get(self):
        '''Get a list of all reviews'''
        return get_facade().get_all_reviews()

    @api.expect(review_model)
    @jwt_required()
    def post(self):
        '''Create a new review'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        if not current_user:
            return {'message': 'Authentication required'}, 401
            
        review_data = api.payload
        # Ensure the review is associated with the current user
        review_data['user_id'] = current_user_id
        
        # Check if user already reviewed this place (prevent duplicate reviews)
        place_id = review_data.get('place_id')
        if place_id:
            place = get_facade().get_place(place_id)
            if not place:
                return {'message': 'Place not found'}, 404
            owner_id_str = str(place.owner_id)
            user_id_str = str(current_user_id)
            if place.owner_id == current_user_id:
                return {'message': 'You cannot review your own place'}, 400
            existing_reviews = get_facade().get_reviews_by_place(place_id)
            for review in existing_reviews:
                if review.user_id == current_user_id:
                    return {'message': 'You have already reviewed this place'}, 400
        
        review = get_facade().create_review(review_data)
        return api.marshal(review, review_model), 201

@api.route('/<string:review_id>')
@api.param('review_id', 'The review identifier')
@api.response(404, 'Review not found')
class ReviewResource(Resource):
    @api.doc('get_review')
    @jwt_required()
    def get(self, review_id):
        '''Get a review given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        review = get_facade().get_review(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        # Check ownership or admin
        if not current_user or (review.user_id != current_user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        return api.marshal(review, review_model)

    @api.expect(review_model)
    @jwt_required()
    def put(self, review_id):
        '''Update a review given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        review = get_facade().get_review(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        # Check ownership or admin
        if not current_user or (review.user_id != current_user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        review_data = api.payload
        # Prevent changing user_id or place_id
        if 'user_id' in review_data:
            del review_data['user_id']
        if 'place_id' in review_data:
            del review_data['place_id']
        updated_review = get_facade().update_review(review_id, review_data)
        if not updated_review:
            return {'message': 'Review not found'}, 404
        return api.marshal(updated_review, review_model)

    @api.response(204, 'Review deleted')
    @jwt_required()
    def delete(self, review_id):
        '''Delete a review given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        review = get_facade().get_review(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        # Check ownership or admin
        if not current_user or (review.user_id != current_user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        deleted = get_facade().delete_review(review_id)
        if not deleted:
            return {'message': 'Review not found'}, 404
        return '', 204

@api.route('/place/<string:place_id>')
@api.param('place_id', 'The place identifier')
@api.response(404, 'Place not found')
class PlaceReviewList(Resource):
    @api.doc('get_reviews_by_place')
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        '''Get all reviews for a particular place'''
        # This endpoint can be public or protected based on requirements
        # For now, let's make it public to allow viewing reviews
        return get_facade().get_reviews_by_place(place_id)
