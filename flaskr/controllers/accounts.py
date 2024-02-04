from flask import jsonify, request
from marshmallow.exceptions import ValidationError
from flaskr.models.accounts import User, Account
from flaskr.schemas.accounts import UserSchema, AccountSchema
from flaskr.database import db
from sqlalchemy.exc import IntegrityError


def create_user_with_account():
    try:
        user = UserSchema().load(request.json, session=db.session)
        db.session.add(user)
        db.session.commit()

        # Use the same session when creating the Account object
        account = Account(user_id=user.id)
        db.session.add(account)
        db.session.commit()
        
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": "Some parameters must be unique"}), 400

    return UserSchema().jsonify(user), 201


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return UserSchema().jsonify(user), 200


def get_all_users():
    users = User.query.all()
    return UserSchema(many=True).jsonify(users), 200
