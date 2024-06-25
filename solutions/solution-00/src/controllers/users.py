from flask import abort, request
from src.data_manager import DataManager
from src.models.user import User


def get_users():
    users = User.get_all()

    return [user.to_dict() for user in users]


def create_user():
    data = request.get_json()

    try:
        new_user = User.create(data)
        DataManager.save_user(new_user)
    except ValueError as e:
        abort(400, str(e))
    
    if new_user is None:
        abort(400, "User already exists")

    return new_user.to_dict(), 201


def get_user_by_id(user_id: str):
    user = DataManager.get_user_by_id(user_id)

    if not user:
        abort(404, f"User with ID {user_id} not found")
    
    return user.to_dict()


def update_user(user_id: str):
    data = request.get_json()

    try:
        user = User.update(user_id, data)
        if user is None:
            abort(404, f"User with ID {user_id} not found")
        
        DataManager.update_user(user_id, data)
    except ValueError as e:
        abort(400, str(e))

    return user.to_dict()


def delete_user(user_id: str):
    success = DataManager.delete_user(user_id) 

    if not success:
        abort(404, f"User with ID {user_id} not found")
    
    return "", 204
