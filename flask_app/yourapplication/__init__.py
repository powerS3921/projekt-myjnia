# yourapplication/__init__.py

from flask import Flask
from yourapplication.extensions import bcrypt, login_manager, db
from yourapplication.models import User  # Adjust based on your actual setup
from yourapplication.extensions import login_manager


def create_app(testing=False):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Initialize extensions
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'routes.login'  # Adjust if your login route is different

    # Initialize database
    db.init_app(app)

    # Register blueprints
    from yourapplication.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
