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
    from flaskr.views.accounts import user_bp
    from flaskr.views.quizzes import quizzes

    app.register_blueprint(user_bp)
    app.register_blueprint(quizzes)

    return app
