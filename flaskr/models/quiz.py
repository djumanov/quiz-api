from flaskr.database import db


class Quiz(db.Model):

    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    def __repr__(self):
        return f'<Quiz {self.title}>'