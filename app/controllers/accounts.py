from flask import jsonify, request

from app.models.accounts import User, Account
from app.schemas.accounts import UserSchema

from app.extensions import db


# Controller for GET /users
def get_all_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    result = user_schema.dump(users)
    return jsonify(result)

# Controller for GET /users/:id
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        user_schema = UserSchema()
        result = user_schema.dump(user)
        return jsonify(result)
    else:
        return jsonify({'message': 'User not found'}), 404

# Controller for POST /users
def create_user():
    data = request.json
    user_schema = UserSchema()
    new_user = user_schema.load(data)
    db.session.add(new_user)
    db.session.commit()
    result = user_schema.dump(new_user)
    return jsonify(result), 201

# Controller for PUT /users/:id
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.json
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.username = data.get('username', user.username)
        user.is_admin = data.get('is_admin', user.is_admin)
        user.is_banned = data.get('is_banned', user.is_banned)
        user.is_active = data.get('is_active', user.is_active)
        db.session.commit()
        user_schema = UserSchema()
        result = user_schema.dump(user)
        return jsonify(result)
    else:
        return jsonify({'message': 'User not found'}), 404

# Controller for DELETE /users/:id
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
