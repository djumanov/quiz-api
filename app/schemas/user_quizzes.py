from app.extensions import ma

from app.models.user_quizzes import UserQuiz


class UserQuizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserQuiz
        load_instance = True
        include_relationships = True
        include_fk = True
