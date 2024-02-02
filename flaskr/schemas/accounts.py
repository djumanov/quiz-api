from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flaskr.models.accounts import Account, User


class AccountSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        load_instance = True
        include_relationships = True
        include_fk = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True
        include_fk = True
