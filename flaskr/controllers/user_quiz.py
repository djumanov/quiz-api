from flask import jsonify, request

from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from flaskr.database import db

from flaskr.models.accounts import User
from flaskr.models.quizzes import UserQuiz, UserAnswer

from flaskr.schemas.accounts import UserSchema
from flaskr.schemas.quizzes import UserQuizSchema, UserAnswerSchema


def create_user_quiz():
    try:
        user_quiz = UserQuizSchema().load(request.json)
        db.session.add(user_quiz)
        db.session.commit()
        return UserQuizSchema().jsonify(user_quiz), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400
    

def get_user_quizzes_by_user_id(user_id):
    user_quizzes = UserQuiz.query.filter_by(user_id=user_id).all()
    return UserQuizSchema(many=True).jsonify(user_quizzes)


def create_user_answer():
    try:
        user_answer = UserAnswerSchema().load(request.json)
        db.session.add(user_answer)
        db.session.commit()
        return UserAnswerSchema().jsonify(user_answer), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400
    

def get_user_answers_by_user_quiz_id(user_quiz_id):
    user_answers = UserAnswer.query.filter_by(user_quiz_id=user_quiz_id).all()
    return UserAnswerSchema(many=True).jsonify(user_answers)
