import unittest
from flask_testing import TestCase
from yourapplication import create_app, db
from yourapplication.models import User
from yourapplication.forms import LoginForm
from werkzeug.security import generate_password_hash

class TestLogin(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # wylaczenie tokenu podczas logowania
        return app

    def setUp(self):
        # Utwórz model użytkownika dla testów
        hashed_password = generate_password_hash('password123', method='sha256')
        user = User(username='testuser', email='test@example.com', password=hashed_password, role='user')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_success(self):
        with self.client:
            response = self.client.post('/login', data=dict(email='test@example.com', password='password123'), follow_redirects=True)
            self.assertIn(b'Welcome back, testuser!', response.data)

    def test_login_failure(self):
        with self.client:
            response = self.client.post('/login', data=dict(email='test@example.com', password='wrongpassword'), follow_redirects=True)
            self.assertIn(b'Login Unsuccessful. Please check email and password', response.data)

if __name__ == '__main__':
    unittest.main()
