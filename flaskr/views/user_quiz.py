from flask import Blueprint

from flaskr.controllers.user_quiz import (
    create_user_quiz, get_user_quizzes_by_user_id,
    create_user_answer, get_user_answers_by_user_quiz_id,
)


user_quiz_bp = Blueprint('user_quiz', __name__)


# get and create user quizzes
user_quiz_bp.add_url_rule('/user-quizzes', 'create_user_quiz', create_user_quiz, methods=['POST'])
user_quiz_bp.add_url_rule('/user-quizzes/<int:user_id>', 'get_user_quizzes_by_user_id', get_user_quizzes_by_user_id, methods=['GET'])

# get and create user answers
user_quiz_bp.add_url_rule('/user-answers', 'create_user_answer', create_user_answer, methods=['POST'])
user_quiz_bp.add_url_rule('/user-answers/<int:user_quiz_id>', 'get_user_answers_by_user_quiz_id', get_user_answers_by_user_quiz_id, methods=['GET'])
