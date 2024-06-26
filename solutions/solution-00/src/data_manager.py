from models import User  # Adjust the import based on your project structure
from app import db, app

class DataManager:
    def __init__(self):
        self.use_database = app.config.get('USE_DATABASE', False)

    def save_user(self, user):
        if self.use_database:
            db.session.add(user)
            db.session.commit()
        else:
            self.save_user_to_file(user)

    def get_user(self, user_id):
        if self.use_database:
            return User.query.get(user_id)
        else:
            return self.get_user_from_file(user_id)

    def save_user_to_file(self, user):
        # Implement the logic to save user to file
        pass

    def get_user_from_file(self, user_id):
        # Implement the logic to get user from file
        pass

    # Implement additional methods for other CRUD operations and models

data_manager = DataManager()
