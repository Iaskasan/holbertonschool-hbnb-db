from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/", methods=["GET"])
@jwt_required()
def get_all_users():
    try:
        # Exemple de vérification de rôle administratif
        current_user = get_jwt_identity()
        if 'admin' not in current_user['roles']:
            return jsonify({"error": "Admin privileges required"}), 403

        # Utilisation de la fonction du contrôleur pour récupérer tous les utilisateurs
        users = get_users()
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@users_bp.route("/", methods=["POST"])
@jwt_required()
def create_new_user():
    try:
        # Exemple de vérification de l'authentification JWT ici si nécessaire
        return create_user(request.json), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@users_bp.route("/<user_id>", methods=["GET"])
@jwt_required()
def get_single_user(user_id):
    try:
        # Exemple de vérification de l'authentification JWT ici si nécessaire
        return get_user_by_id(user_id), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 404

@users_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
def update_existing_user(user_id):
    try:
        # Exemple de vérification de rôle administratif
        current_user = get_jwt_identity()
        if 'admin' not in current_user['roles']:
            return jsonify({"error": "Admin privileges required"}), 403

        # Utilisation de la fonction du contrôleur pour mettre à jour l'utilisateur
        return update_user(user_id, request.json), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@users_bp.route("/<user_id>", methods=["DELETE"])
@jwt_required()
def delete_existing_user(user_id):
    try:
        # Exemple de vérification de rôle administratif
        current_user = get_jwt_identity()
        if 'admin' not in current_user['roles']:
            return jsonify({"error": "Admin privileges required"}), 403

        # Utilisation de la fonction du contrôleur pour supprimer l'utilisateur
        return delete_user(user_id), 204

    except Exception as e:
        return jsonify({"error": str(e)}), 400
