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
    from flaskr.main import bp as main_bp
    app.register_blueprint(main_bp)


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

