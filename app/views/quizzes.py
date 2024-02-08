from flask import Blueprint
from app.controllers.quizzes import get_all_technologies, get_quizzes_by_technology_id, get_questions_by_quiz_id, get_answers_by_question_id

# Create a Blueprint for the quizzes-related endpoints
quizzes_blueprint = Blueprint('quizzes', __name__)


# Define routes for the endpoints
quizzes_blueprint.route('/technologies', methods=['GET'])(get_all_technologies)
quizzes_blueprint.route('/technologies/<int:tech_id>/quizzes', methods=['GET'])(get_quizzes_by_technology_id)
quizzes_blueprint.route('/quizzes/<int:quiz_id>/questions', methods=['GET'])(get_questions_by_quiz_id)
quizzes_blueprint.route('/questions/<int:question_id>/answers', methods=['GET'])(get_answers_by_question_id)
