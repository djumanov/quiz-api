from flask import Blueprint
from flaskr.controllers.quizzes import (
    get_all_quizzes,
    get_quiz_by_id,
    create_quiz,
    update_quiz,
    delete_quiz,
)


quiz_bp = Blueprint('quiz', __name__, url_prefix='/quizzes')

@quiz_bp.route('/', methods=['GET'])
def view_get_all_quizzes():
    return get_all_quizzes()

@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def view_get_quiz_by_id(quiz_id):
    return get_quiz_by_id(quiz_id)

@quiz_bp.route('/', methods=['POST'])
def view_create_quiz():
    return create_quiz()

@quiz_bp.route('/<int:quiz_id>', methods=['PUT'])
def view_update_quiz(quiz_id):
    return update_quiz(quiz_id)

@quiz_bp.route('/<int:quiz_id>', methods=['DELETE'])
def view_delete_quiz(quiz_id):
    return delete_quiz(quiz_id)
