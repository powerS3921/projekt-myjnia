from flask_sqlalchemy import SQLAlchemy

class DatabaseSingleton:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.db = SQLAlchemy(app)
        return cls._instance

    @classmethod
    def get_instance(cls, app=None):
        if cls._instance is None:
            cls._instance = DatabaseSingleton(app)
        return cls._instance.db
