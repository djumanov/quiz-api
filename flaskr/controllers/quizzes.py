from flask import jsonify, request
from marshmallow import ValidationError
from flaskr.database import db
from flaskr.models.quiz import Quiz
from flaskr.schemas.quizzes import QuizSchema

def get_all_quizzes():
    quizzes = Quiz.query.all()
    quiz_schema = QuizSchema(many=True)
    result = quiz_schema.dump(quizzes)
    return jsonify(result)

def get_quiz_by_id(quiz_id):
    quiz = Quiz.query.get(quiz_id)

    if not quiz:
        return jsonify({'message': 'Quiz not found'}), 404

    quiz_schema = QuizSchema()
    result = quiz_schema.dump(quiz)
    return jsonify(result)

def create_quiz():
    data = request.json

    try:
        quiz_schema = QuizSchema()
        validated_data = quiz_schema.load(data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    new_quiz = Quiz(**validated_data)

    db.session.add(new_quiz)
    db.session.commit()

    result = quiz_schema.dump(new_quiz)
    return jsonify(result), 201

def update_quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)

    if not quiz:
        return jsonify({'message': 'Quiz not found'}), 404

    data = request.json

    try:
        quiz_schema = QuizSchema()
        validated_data = quiz_schema.load(data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    for key, value in validated_data.items():
        setattr(quiz, key, value)

    db.session.commit()

    result = quiz_schema.dump(quiz)
    return jsonify(result)

def delete_quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)

    if not quiz:
        return jsonify({'message': 'Quiz not found'}), 404

    db.session.delete(quiz)
    db.session.commit()

    return jsonify({'message': 'Quiz deleted successfully'})
