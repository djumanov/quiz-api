from flaskr.database import ma

from flaskr.models.accounts import Account, User


class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        load_instance = True
        include_relationships = True
        include_fk = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True
        include_fk = True
