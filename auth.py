from flask import Blueprint, jsonify, request, make_response
from . import db
from .models import *
import random, uuid
from .utils import *

auth = Blueprint('auth', __name__)


@auth.route('/success', methods=['GET'])
def login_success():
    return jsonify('Success!')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # register()
    response_object = {"status": False}
    if request.method == 'POST':
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        pw = password
        pw = encrypt_password(str(password))
        user = User.query.filter_by(email=email, password=pw).first()
        # if user exists
        if user:
            response_object["status"] = True
            response_object["message"] = "Login success!"
            response_object["user_id"] = user.user_id
        else:
            response_object["message"] = "Incorrect email/password!"
    return jsonify(response_object)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')

    # Check if valid
    content = {}
    content['username'] = username
    content['email'] = email
    content['password'] = password

    response_object = {}
    message, status = checkregister(content)
    response_object["status"] = status
    response_object["message"] = message
    if status is not True:
        return jsonify(response_object)

    # Check if already exist
    pw = encrypt_password(password)
    user1 = User.query.filter_by(email=email).first()
    if user1:
        print("Email occupied!")
        response_object["status"] = False
        response_object["message"] = "Email occupied!"
    else:
        new_user = User(user_id=str(uuid.uuid4()), username=username, email=email, password=pw)
        try:
            db.session.add(new_user)
            db.session.commit()
            print("Registered!")
            response_object["message"] = "Registered!"
            response_object["user_id"] = new_user.user_id
        except Exception as e:
            print(e)
            response_object["status"] = False
            response_object["message"] = "Registered failed"
    return jsonify(response_object)