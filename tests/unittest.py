import unittest
from app import app, db, User

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

if __name__ == '__main__':
    unittest.main()
