from flask import Blueprint, jsonify, request
from flaskr.controllers.accounts import get_all_users, get_user_by_id, create_user, update_user, delete_user


user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET', 'POST'])
def view_get_all_users():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        return create_user()

@user_bp.route('/<int:user_id>', methods=['GET'])
def view_get_user_by_id(user_id):
    return get_user_by_id(user_id)

# @user_bp.route('/', methods=['POST'])
# def view_create_user():
#     return create_user()

@user_bp.route('/<int:user_id>', methods=['PUT'])
def view_update_user(user_id):
    return update_user(user_id)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def view_delete_user(user_id):
    return delete_user(user_id)
