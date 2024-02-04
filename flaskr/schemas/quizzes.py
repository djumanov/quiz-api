from flaskr.database import ma

from flaskr.models.quizzes import Language, Quiz, QustionType, Question, Answer, UserQuiz, UserAnswer


class LanguageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Language
        include_fk = True
        load_instance = True


class QuizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quiz
        include_fk = True
        load_instance = True


class QustionTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QustionType
        include_fk = True
        load_instance = True


class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        include_fk = True
        load_instance = True


class AnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Answer
        include_fk = True
        load_instance = True


class UserQuizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserQuiz
        include_fk = True
        load_instance = True


class UserAnswerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserAnswer
        include_fk = True
        load_instance = True
