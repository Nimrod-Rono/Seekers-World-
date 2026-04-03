from flask import Blueprint, request, jsonify
from your_application import db, jwt
from your_application.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])  # Make sure to hash password
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()  # Add validation for password
    if user:
        # Normally you would return a token
        return jsonify({'token': 'fake_token'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/validate', methods=['GET'])
def validate_token():
    # Assume we get token from headers
    token = request.headers.get('Authorization')
    if token is None:
        return jsonify({'message': 'Token is missing!'}), 403
    # Token validation logic here
    return jsonify({'message': 'Token is valid'}), 200
