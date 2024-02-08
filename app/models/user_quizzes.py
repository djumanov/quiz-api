from datetime import datetime

from sqlalchemy.orm import validates

from app.extensions import db


class UserQuiz(db.Model):
    __tablename__ = 'user_quizzes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    correct_answers = db.Column(db.Integer, default=0)
    incorrect_answers = db.Column(db.Integer, default=0)
    missed_answers = db.Column(db.Integer, default=0)
    total_questions = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float)
    time = db.Column(db.Integer)
    is_finished = db.Column(db.Boolean, default=False)
    is_passed = db.Column(db.Boolean, default=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime)

    user = db.relationship('User', backref='user_quizzes')
    quiz = db.relationship('Quiz', backref='user_quizzes')

    @validates('correct_answers', 'incorrect_answers', 'missed_answers')
    def validate_answers(self, key, value):
        if value <= 0:
            raise ValueError("Answers count must be greater than 0.")
        if key == 'correct_answers' and value >= self.total_questions:
            raise ValueError("Correct answers count must be less than questions count.")
        if key == 'incorrect_answers' and value >= self.total_questions:
            raise ValueError("Incorrect answers count must be less than questions count.")
        if key == 'missed_answers' and value >= self.total_questions:
            raise ValueError("Missed answers count must be less than questions count.")
        return value

    @validates('score')
    def validate_score(self, key, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        return score

    @validates('time')
    def validate_time(self, key, time):
        if time <= 0:
            raise ValueError("Time must be greater than 0.")
        return time
