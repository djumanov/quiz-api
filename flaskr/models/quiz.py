from flaskr.database import db
from flaskr.models.accounts import User, Account


class Language(db.Model):

    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Language {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    

class Quiz(db.Model):

    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    language = db.relationship('Language', backref=db.backref('quizzes', lazy=True))

    def __repr__(self):
        return f'<Quiz {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'language_id': self.language_id
        }
    

class QustionType(db.Model):
    
    __tablename__ = 'question_type'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<QuestionType {self.type}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type
        }
    

class Question(db.Model):
    
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), nullable=False, unique=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    quiz = db.relationship('Quiz', backref=db.backref('questions', lazy=True))
    type_id = db.Column(db.Integer, db.ForeignKey('question_type.id'), nullable=False)
    type = db.relationship('QustionType', backref=db.backref('questions', lazy=True))

    def __repr__(self):
        return f'<Question {self.question}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'quiz_id': self.quiz_id,
            'type_id': self.type_id
        }
    
    def get_answers(self):
        return [answer.to_dict() for answer in self.answers]


class Answer(db.Model):
    
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question = db.relationship('Question', backref=db.backref('answers', lazy=True))

    def __repr__(self):
        return f'<Answer {self.answer}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'answer': self.answer,
            'is_correct': self.is_correct,
            'question_id': self.question_id
        }
    

class UserQuiz(db.Model):
        
    __tablename__ = 'user_quiz'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('user_quizzes', lazy=True))
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    quiz = db.relationship('Quiz', backref=db.backref('user_quizzes', lazy=True))
    score = db.Column(db.Float, nullable=False, default=0)
    taken_at = db.Column(db.DateTime, server_default=db.func.now())
    submitted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<UserQuiz {self.user_id} - {self.quiz_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'quiz_id': self.quiz_id,
            'score': self.score,
            'taken_at': self.taken_at,
            'submitted_at': self.submitted_at
        }
    
    def update_score(self, score: float) -> float:
        self.score = score
        return self.score
    
    def submit(self):
        self.submitted_at = db.func.now()
        return self.submitted_at
       

class UserAnswer(db.Model):
        
    __tablename__ = 'user_answer'

    id = db.Column(db.Integer, primary_key=True)
    user_quiz_id = db.Column(db.Integer, db.ForeignKey('user_quiz.id'), nullable=False)
    user_quiz = db.relationship('UserQuiz', backref=db.backref('user_answers', lazy=True))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    question = db.relationship('Question', backref=db.backref('user_answers', lazy=True))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    answer = db.relationship('Answer', backref=db.backref('user_answers', lazy=True))
    answered_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<UserAnswer {self.user_quiz_id} - {self.question_id} - {self.answer_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_quiz_id': self.user_quiz_id,
            'question_id': self.question_id,
            'answer_id': self.answer_id,
            'answered_at': self.answered_at
        }
    