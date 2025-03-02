from flask import Blueprint, request, jsonify
import requests
import os
import Users
from CreateUser import USERS_DATABASE

loginuser = Blueprint('loginuser', __name__)
@loginuser.route('/', methods=['POST'])
def login_user():
    username = request.json['username']
    password = request.json['password']
    if username not in USERS_DATABASE:
        return jsonify({"success": False, "message": "Username not found!"}), 400
    if USERS_DATABASE[username].password != password:
        return jsonify({"success": False, "message": "Incorrect password!"}), 400
    user = USERS_DATABASE[username]
    return jsonify({
        "success": True,
        "message": "Login successful!",
        "user": {
            "username": username
        }
    }), 200