from flaskr.main import bp

from flaskr.database import db
from flaskr.models.quiz import Quiz

@bp.route('/')
def index():
    quizs = Quiz.query.all()
    results = [quiz.title for quiz in quizs]
    return '<br>'.join(results)

@bp.route('/populate-db/')
def populate_db():
    quiz1 = Quiz(title='Quiz 1')
    quiz2 = Quiz(title='Quiz 2')
    quiz3 = Quiz(title='Quiz 3')
    db.session.add(quiz1)
    db.session.add(quiz2)
    db.session.add(quiz3)
    db.session.commit()
    return 'Database populated!'