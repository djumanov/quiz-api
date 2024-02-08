from flask import jsonify, request

from app.models.user_quizzes import UserQuiz
from app.schemas.user_quizzes import UserQuizSchema

from app.extensions import db


# Controller for GET /user-quizzes
def get_all_user_quizzes():
    user_quizzes = UserQuiz.query.all()
    user_quiz_schema = UserQuizSchema(many=True)
    result = user_quiz_schema.dump(user_quizzes)
    return jsonify(result)

# Controller for GET /user-quizzes/:id
def get_user_quiz_by_id(user_quiz_id):
    user_quiz = UserQuiz.query.get(user_quiz_id)
    if user_quiz:
        user_quiz_schema = UserQuizSchema()
        result = user_quiz_schema.dump(user_quiz)
        return jsonify(result)
    else:
        return jsonify({'message': 'User quiz not found'}), 404

# Controller for POST /user-quizzes
def create_user_quiz():
    data = request.json
    user_quiz_schema = UserQuizSchema()
    new_user_quiz = user_quiz_schema.load(data)
    db.session.add(new_user_quiz)
    db.session.commit()
    result = user_quiz_schema.dump(new_user_quiz)
    return jsonify(result), 201
