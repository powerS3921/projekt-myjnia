# yourapplication/extensions.py

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
login_manager = LoginManager()
db = SQLAlchemy()  # Initialize SQLAlchemy instance
def load_user(user_id):
    return User.query.get(int(user_id))