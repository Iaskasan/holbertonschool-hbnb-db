from src.persistence import db  # Adjust the import based on your project structure
from src.models import User  # Adjust the import based on your project structure

class DataManager:
    def __init__(self):
        self.repository = db

    def save_user(self, user):
        self.repository.save(user)

    def get_user(self, user_id):
        return self.repository.get("User", user_id)

    def update_user(self, user):
        return self.repository.update(user)

    def delete_user(self, user):
        return self.repository.delete(user)

    # Implement additional methods for other CRUD operations and models

data_manager = DataManager()