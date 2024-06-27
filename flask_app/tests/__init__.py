from flask import Flask
from yourapplication.database import DatabaseSingleton
from yourapplication.extensions import bcrypt, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Inicjalizacja rozszerzeń
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Inicjalizacja bazy danych za pomocą Singleton
    db = DatabaseSingleton.get_instance(app)

    with app.app_context():
        from yourapplication import routes  # Importowanie poza funkcją route, aby uniknąć cyklicznego importu
        from yourapplication.tests import test_register, test_login, test_logout, test_carwash  # Importujemy testy z folderu tests
    
    return app
