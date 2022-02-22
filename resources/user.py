# the resources are basically an external representation that interacts with the API.
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):  # This is to prevent duplicate usernames
            return {'message': 'A user with this username already exists'}, 400

        data = UserModel(**data)  # Same as UserModel(data['username'], data['password'])
        data.save_to_db()

        return {'message': 'User successfully created'}, 201
