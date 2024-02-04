from flask import Blueprint
from flaskr.controllers.quizzes import (
    create_language, get_languages, 
    create_quiz, get_quizzes_by_language,
    create_question_type, get_question_types,
    create_question, get_questions_by_quiz, 
    create_answer, get_answers_by_question,
)

quizzes = Blueprint('quizzes', __name__)


# get and create languages
quizzes.add_url_rule('/languages', 'get_languages', get_languages, methods=['GET'])
quizzes.add_url_rule('/languages', 'create_language', create_language, methods=['POST'])

# get and create quizzes
quizzes.add_url_rule('/quizzes', 'create_quiz', create_quiz, methods=['POST'])
quizzes.add_url_rule('/quizzes/<int:language_id>', 'get_quizzes_by_language', get_quizzes_by_language, methods=['GET'])

# get and create question types
quizzes.add_url_rule('/question_types', 'create_question_type', create_question_type, methods=['POST'])
quizzes.add_url_rule('/question_types', 'get_question_types', get_question_types, methods=['GET'])

# get and create questions
quizzes.add_url_rule('/quizzes/<int:quiz_id>/questions', 'create_question', create_question, methods=['POST'])
quizzes.add_url_rule('/quizzes/<int:quiz_id>/questions', 'get_questions_by_quiz', get_questions_by_quiz, methods=['GET'])

# get and create answers
quizzes.add_url_rule('/questions/<int:question_id>/answers', 'create_answer', create_answer, methods=['POST'])
quizzes.add_url_rule('/questions/<int:question_id>/answers', 'get_answers_by_question', get_answers_by_question, methods=['GET'])
