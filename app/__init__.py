from flask import Flask

from app.config import CONFIGS

from app.extensions import init_app


def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    # load the config
    config_name = app.config.get('FLASK_ENV', 'development')
    app.config.from_object(CONFIGS[config_name])

    # Initialize extensions within the app context
    with app.app_context():
        init_app(app)

    # import and register the error handlers
    from app.errors import errors_bp
    app.register_blueprint(errors_bp)

    # import and register the accounts blueprint
    from app.views.accounts import accounts_blueprint
    app.register_blueprint(accounts_blueprint)

    # import and register the quizzes blueprint
    from app.views.quizzes import quizzes_blueprint
    app.register_blueprint(quizzes_blueprint)
    
    return app
