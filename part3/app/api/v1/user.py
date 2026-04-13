from flask_restx import Namespace, Resource, fields # Imports the tools to build/define API endpoints
from flask import current_app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.blayer.user import User

api = Namespace('user', description = 'User operations') #Creates a namespace grouping all user related endpoints together under one path

# Get facade from app context
def get_facade():
    return current_app.facade

#Converts user profile in JSON for API - exclude password from responses by default
user_model = api.model ('User', 
    {
    'id': fields.String(readOnly=True, description='The user unique identifier'),
    'first_name': fields.String(required=True, description='First name of the user'), # First name is mandatory, can't be left blank
    'last_name': fields.String(required=True, description='Last name of the user'),# Last name is mandatory, cant be left blank
    'email': fields.String(required=True, description='Email address of the user'), # Email is mandatory, can't be blank
    'is_admin': fields.Boolean(description='Admin privileges'),
    })

# Model for user creation/update (includes password)
user_input_model = api.model ('UserInput', 
    {
    'id': fields.String(readOnly=True, description='The user unique identifier'),
    'first_name': fields.String(required=True, description='First name of the user'), # First name is mandatory, can't be left blank
    'last_name': fields.String(required=True, description='Last name of the user'),# Last name is mandatory, cant be left blank
    'email': fields.String(required=True, description='Email address of the user'), # Email is mandatory, can't be blank
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(description='Admin privileges'),
    })

user_login_model = api.model('UserLogin', {
    'email': fields.String(required=True, description='Email address of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

@api.route('/')
class UserList(Resource):
    @api.doc('get_users', security='Bearer Auth')
    @jwt_required()
    def get(self):
        '''Get a list of all users (admin only)'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        if not current_user or not current_user.is_admin:
            return {'message': 'Admin access required'}, 403
        users = get_facade().get_all_users()
        return [api.marshal(user, user_model) for user in users]

    @api.expect(user_input_model)
    @jwt_required(optional=True)
    @api.doc(security=[])
    def post(self):
        '''Create a new user'''
        user_data = api.payload
        user_count = User.query.count()
        if user_count == 0:
            # First user: no auth required, and we set them as admin
            user_data['is_admin'] = True
        else:
            # Subsequent users: require admin auth
            current_user_id = get_jwt_identity()
            current_user = get_facade().get_user(current_user_id)
            if not current_user or not current_user.is_admin:
                return {'message': 'Admin access required'}, 403

        user = get_facade().create_user(user_data)
        return api.marshal(user, user_model), 201

@api.route('/<string:user_id>')
@api.param('user_id', 'The user identifier')
@api.response(404, 'User not found')
class UserResource(Resource):
    @api.doc('get_user')
    @jwt_required()
    def get(self, user_id):
        '''Get a user given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        # Users can only get their own profile, admins can get any
        if not current_user or (current_user.id != user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        user = get_facade().get_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return api.marshal(user, user_model)

    @api.expect(user_input_model)
    @jwt_required()
    @api.doc(security='Bearer Auth')
    def put(self, user_id):
        '''Update a user given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        # Users can only update their own profile, admins can update any
        if not current_user or (current_user.id != user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        user_data = api.payload
        # Prevent non-admins from changing is_admin flag
        if not current_user.is_admin and 'is_admin' in user_data:
            del user_data['is_admin']
        updated_user = get_facade().update_user(user_id, user_data)
        if not updated_user:
            return {'message': 'User not found'}, 404
        return api.marshal(updated_user, user_model)

    @api.response(200, 'User deleted')
    @jwt_required()
    @api.doc(security='Bearer Auth')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        current_user_id = get_jwt_identity()
        current_user = get_facade().get_user(current_user_id)
        # Users can only delete their own account, admins can delete any
        if not current_user or (current_user.id != user_id and not current_user.is_admin):
            return {'message': 'Unauthorized access'}, 403
        deleted = get_facade().delete_user(user_id)
        if not deleted:
            return {'message': 'User not found'}, 404
        return {'message': 'User successfully deleted'}, 200

@api.route('/login')
class UserLogin(Resource):
    @api.doc('login_user', security=[])
    @api.expect(user_login_model)
    def post(self):
        '''Login a user and return JWT token'''
        login_data = api.payload
        email = login_data.get('email')
        password = login_data.get('password')

        # Find user by email
        user = get_facade().get_user_by_email(email)
        if not user:
            return {'message': 'Invalid credentials'}, 401

        # Check password using bcrypt
        if not user.check_password(password):
            return {'message': 'Invalid credentials'}, 401
            
        # Generate JWT token using flask-jwt-extended
        access_token = create_access_token(identity=user.id, additional_claims={'is_admin': user.is_admin})
         
        return {
            'access_token': access_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }




