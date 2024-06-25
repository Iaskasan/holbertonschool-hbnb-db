from src import db
from src.models.user import User
import os

class DataManager:
    @staticmethod
    def save_user(user):
        if os.getenv('USE_DATABASE') == 'True':
            db.session.add(user)
            db.session.commit()
        else:
            pass

    @staticmethod
    def get_user_by_id(user_id):
        if os.getenv('USE_DATABASE') == 'True':
            return User.query.get(user_id)
        else:
            # Implement file-based retrieval logic if needed
            pass

    @staticmethod
    def get_all_users():
        if os.getenv('USE_DATABASE') == 'True':
            return User.query.all()
        else:
            pass
    
    @staticmethod
    def update_user(user_id, data):
        if os.getenv('USE_DATABASE') == 'True':
            user = User.query.get(user_id)

            if not user:
                return None

            if "email" in data:
                user.email = data["email"]
            if "password" in data:
                user.password = data["password"]
            if "is_admin" in data:
                user.is_admin = data["is_admin"]

            db.session.commit()
        else:
            pass

    @staticmethod
    def delete_user(user_id):
        if os.getenv('USE_DATABASE') == 'True':
            user = User.query.get(user_id)

            if not user:
                return False

            db.session.delete(user)
            db.session.commit()
        else:
            pass
    
    @staticmethod
    def create_user(user_data):
        if os.getenv('USE_DATABASE') == 'True':
            email = user_data.get("email")
            password = user_data.get("password")
            is_admin = user_data.get("is_admin", False)

            new_user = User(email=email, password=password, is_admin=is_admin)
            db.session.add(new_user)
            db.session.commit()
        else:
            pass
    
