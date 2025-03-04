from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.utils.database import db
import datetime

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    # Get the data from the frontend
    data = request.form
    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'],
                    password=hashed_password, email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.form
    print(data)
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login failed"}), 401

    # If login is successful, create a response object
    response = make_response(jsonify(
        {"userId": user.id, "email": user.email, "username": user.username}), 200)

    # Set a cookie with the user's ID or some session token
    expires = datetime.datetime.now() + datetime.timedelta(days=7)
    response.set_cookie('user_id', str(user.id),
                        expires=expires, httponly=True)

    return response
