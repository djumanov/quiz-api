from flask import jsonify, request

from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from flaskr.database import db

from flaskr.models.quiz import Language, Quiz, QustionType, Question, Answer

from flaskr.schemas.quizzes import LanguageSchema, QuizSchema, QustionTypeSchema, QuestionSchema, AnswerSchema



def create_language():
    try:
        language = LanguageSchema().load(request.json)
        db.session.add(language)
        db.session.commit()
        return LanguageSchema().jsonify(language), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400


def get_languages():
    languages = Language.query.all()
    return LanguageSchema(many=True).jsonify(languages)


def create_quiz():
    try:
        quiz = QuizSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400

    db.session.add(quiz)
    db.session.commit()

    return QuizSchema().jsonify(quiz), 201


def get_quizzes_by_language(language_id):
    quizzes = Quiz.query.filter_by(language_id=language_id).all()
    return QuizSchema(many=True).jsonify(quizzes)


def create_question_type():
    try:
        question_type = QustionTypeSchema().load(request.json)
        db.session.add(question_type)
        db.session.commit()
        return QustionTypeSchema().jsonify(question_type), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400


def get_question_types():
    question_types = QustionType.query.all()
    return QustionTypeSchema(many=True).jsonify(question_types)


def create_question(quiz_id):
    try:
        # add quiz_id to the request.json
        request.json['quiz_id'] = quiz_id

        question = QuestionSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400

    db.session.add(question)
    db.session.commit()

    return QuestionSchema().jsonify(question), 201


def get_questions_by_quiz(quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    return QuestionSchema(many=True).jsonify(questions)


def create_answer(question_id):
    try:
        # add question_id to the request.json
        request.json['question_id'] = question_id
        
        answer = AnswerSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400

    db.session.add(answer)
    db.session.commit()

    return AnswerSchema().jsonify(answer), 201


def get_answers_by_question(question_id):
    answers = Answer.query.filter_by(question_id=question_id).all()
    return AnswerSchema(many=True).jsonify(answers)
