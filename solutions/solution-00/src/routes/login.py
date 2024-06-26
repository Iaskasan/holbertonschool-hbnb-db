from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from src.models import User
from src import bcrypt

login_bp = Blueprint("login", __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Invalid email or password'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid email or password'}), 400

    # Création du JWT avec l'identifiant de l'utilisateur
    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200
