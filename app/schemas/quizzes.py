from app.extensions import ma

from app.models.quizzes import (
    Technology,
    Quiz,
    Question,
    Option,
)


class TechnologySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Technology
        load_instance = True
        include_relationships = True
        include_fk = True


class QuizSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quiz
        load_instance = True
        include_relationships = True
        include_fk = True


class QuestionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        load_instance = True
        include_relationships = True
        include_fk = True


class OptionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Option
        load_instance = True
        include_relationships = True
        include_fk = True
