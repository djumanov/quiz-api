from flask import jsonify

from app.models.quizzes import Technology, Quiz, Question, Option
from app.schemas.quizzes import TechnologySchema, QuizSchema, QuestionSchema, OptionSchema


# Controller for GET /technologies
def get_all_technologies():
    technologies = Technology.query.all()
    technology_schema = TechnologySchema(many=True)
    result = technology_schema.dump(technologies)
    return jsonify(result)

# Controller for GET /technologies/:id/quizzes
def get_quizzes_by_technology_id(tech_id):
    quizzes = Quiz.query.filter_by(technology_id=tech_id).all()
    quiz_schema = QuizSchema(many=True)
    result = quiz_schema.dump(quizzes)
    return jsonify(result)

# Controller for GET /quizzes/:id/questions
def get_questions_by_quiz_id(quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    question_schema = QuestionSchema(many=True)
    result = question_schema.dump(questions)
    return jsonify(result)

# Controller for GET /questions/:id/answers
def get_answers_by_question_id(question_id):
    options = Option.query.filter_by(question_id=question_id).all()
    option_schema = OptionSchema(many=True)
    result = option_schema.dump(options)
    return jsonify(result)
