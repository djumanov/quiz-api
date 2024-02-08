from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

from app.extensions import db


class Technology(db.Model):
    __tablename__ = 'technologies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    quizzes = db.relationship('Quiz', backref='technology', lazy=True)


class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('technologies.id'))
    quiz = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    questions = db.relationship('Question', backref='quiz', lazy=True)


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    question = db.Column(db.String(length=300), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    options = db.relationship('Option', backref='question', lazy=True)

    @validates('level')
    def validate_level(self, key, level):
        if level < 1 or level > 5:
            raise ValueError('Level must be between 1 and 5')
        return level
    
    __table_args__ = (
        CheckConstraint('level >= 1 AND level <= 5', name='check_level'),
    )


class Option(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    option = db.Column(db.String(length=100), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

    @validates('is_correct')
    def validate_correct_option(self, key, is_correct):
        # Ensure that the number of correct options for each question does not exceed 1
        if is_correct and Option.query.filter_by(question_id=self.question_id, is_correct=True).count() > 0:
            raise ValueError("Only one correct option is allowed per question.")
        return is_correct
    
    __table_args__ = (
        CheckConstraint('is_correct IN (0, 1)', name='check_is_correct'),
    )


# The Technology model represents the different technologies that the quizzes are based on.
# The Quiz model represents the quizzes for each technology.
# The Question model represents the questions for each quiz.
# The Option model represents the options for each question.
# The @validates decorator is used to validate the level attribute of the Question model.
# The CheckConstraint is used to enforce the level attribute to be between 1 and 5.
# The @validates decorator is used to validate the is_correct attribute of the Option model.
# The CheckConstraint is used to enforce the is_correct attribute to be either 0 or 1.
# The Option model also has a custom validation to ensure that only one correct option is allowed per question.