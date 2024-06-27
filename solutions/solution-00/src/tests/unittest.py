import unittest
from src.app import app, db
from src.models.user import User  # Assuming User model is defined in src.models

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user = User(email="test@example.com", password="password")
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().email, "test@example.com")
        self.assertNotEqual(User.query.first().password, "password")  # Assuming password is hashed

    def test_query_user(self):
        user = User(email="query@example.com", password="password")
        db.session.add(user)
        db.session.commit()
        queried_user = User.query.filter_by(email="query@example.com").first()
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email, "query@example.com")

    def test_update_user(self):
        user = User(email="update@example.com", password="password")
        db.session.add(user)
        db.session.commit()
        user.email = "updated@example.com"
        user.password = "newpassword"  # Assuming password hashing is handled automatically
        db.session.commit()
        updated_user = User.query.filter_by(email="updated@example.com").first()
        self.assertIsNotNone(updated_user)
        self.assertNotEqual(updated_user.password, "newpassword")

    def test_delete_user(self):
        user = User(email="delete@example.com", password="password")
        db.session.add(user)
        db.session.commit()
        db.session.delete(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 0)

if __name__ == '__main__':
    unittest.main()