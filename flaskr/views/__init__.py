from flaskr.views.accounts import accounts_bp
from flaskr.views.quizzes import quizzes_bp


def register_blueprints(app):
    app.register_blueprint(accounts_bp)
    app.register_blueprint(quizzes_bp)
