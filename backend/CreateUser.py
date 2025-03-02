from flask import Blueprint, request, jsonify
import requests
import os
import Users

# Store users in a dictionary
USERS_DATABASE = {}

createuser = Blueprint('createuser', __name__)
@createuser.route('/', methods=['POST'])
def create_user():
    username = request.json['username']
    if username in USERS_DATABASE:
        return jsonify({"success": False, "message": "Username already exists!"}), 400
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    password = request.json['password']
    address = request.json['address']
    if len(address[3]) != 2:
        return jsonify({"success": False, "message": "Invalid state abbreviation!"}), 400
    if len(address[4]) != 5:
        return jsonify({"success": False, "message": "Invalid zip code!"}), 400
    balance = request.json.get('balance', '0')
    try:
        balance = float(balance)
        if balance < 0:
            return jsonify({"success": False, "message": "Balance cannot be negative!"}), 400
    except ValueError:
        return jsonify({"success": False, "message": "Invalid balance format. Must be a number!"}), 400
    user = Users.User(username, firstname, lastname, password, address, balance)
    USERS_DATABASE[username] = user
    return jsonify({
            "success": True,
            "message": "Accounted created successfully!!",
            "user": {
                "username": username
            }
        }), 201