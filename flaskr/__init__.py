from flask import Flask
from flask_migrate import Migrate

from flaskr.config import Config
from flaskr.database import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints here
    from flaskr.views.accounts import accounts_bp
    from flaskr.views.quizzes import quizzes_bp
    from flaskr.views.user_quiz import user_quiz_bp

    app.register_blueprint(accounts_bp)
    app.register_blueprint(quizzes_bp)
    app.register_blueprint(user_quiz_bp)
    
    return app
