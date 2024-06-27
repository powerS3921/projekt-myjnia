import unittest
from flask_testing import TestCase
from flask_app.yourapplication import create_app, db
from flask_app.yourapplication.models import User, UserFacade

class TestRegistration(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_new_user(self):
        response = self.client.post('/register', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }, follow_redirects=True)

        self.assertIn(b'Your account has been created!', response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.query.filter_by(username='testuser').first() is not None)

if __name__ == '__main__':
    unittest.main()

