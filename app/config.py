import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY') # Set SECRET_KEY in .env
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///quiz.db')  # Default to 'sqlite:///quiz.db' if SQLALCHEMY_DATABASE_URI is not set in .env
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)  # Default to False if SQLALCHEMY_TRACK_MODIFICATIONS is not set in .env
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO', False)  # Default to False if SQLALCHEMY_ECHO is not set in .env


class DevelopmentConfig(Config):
    # Development Config
    DEBUG = False
    TESTING = False
    FLASK_RUN_HOST = 'localhost'
    FLASK_RUN_PORT = 5000
    SQLALCHEMY_ECHO = True



class TestingConfig(Config):
    # Testing Config
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    # Production Config
    DEBUG = False
    TESTING = False
    FLASK_RUN_HOST = 'localhost'
    FLASK_RUN_PORT = 5000
    SQLALCHEMY_ECHO = False


CONFIGS = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
