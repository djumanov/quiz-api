from flaskr.database import db


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.Integer, nullable=False, unique=True)
    phone_number = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(100), nullable=True, unique=True)

    @property
    def full_name(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name
    
    def __repr__(self):
        return f'<User {self.full_name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'telegram_id': self.telegram_id,
            'phone_number': self.phone_number,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username
        }
    

class Account(db.Model):
    
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('accounts', lazy=True))
    balance = db.Column(db.Float, nullable=False, default=0)

    def __repr__(self):
        return f'<Account {self.user.full_name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'balance': self.balance
        }
    
    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        return self.balance
    