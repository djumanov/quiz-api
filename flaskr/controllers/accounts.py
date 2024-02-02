from flask import jsonify, request
from marshmallow.exceptions import ValidationError
from flaskr.models.accounts import User
from flaskr.schemas.accounts import UserSchema
from flaskr.database import db


# Initialize UserSchema
user_schema = UserSchema()

def get_all_users():
    users = User.query.all()
    result = user_schema.dump(users, many=True)
    return jsonify(result)

def get_user_by_id(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    result = user_schema.dump(user)
    return jsonify(result)

def create_user():
    data = request.json

    try:
        # Access the Flask application context to get the SQLAlchemy session
        with db.session.no_autoflush:
            # Validate incoming data using the UserSchema and pass the session
            user = user_schema.load(data, session=db.session)
            print(user)

    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    # Add the user to the session and commit the changes
    db.session.add(user)
    db.session.commit()

    # create the account for the user
    user.create_account()


    result = user_schema.dump(user)
    return jsonify(result), 201

def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json

    try:
        # Validate incoming data using the UserSchema
        validated_data = user_schema.load(data)
    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    # Update user properties with the validated data
    for key, value in validated_data.items():
        setattr(user, key, value)

    db.session.commit()

    result = user_schema.dump(user)
    return jsonify(result)

def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'})
