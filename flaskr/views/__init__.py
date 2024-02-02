from flaskr.views.accounts import user_bp
from flaskr.views.quizzes import quiz_bp


def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(quiz_bp)
