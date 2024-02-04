from flask import Blueprint

from flaskr.controllers.accounts import create_user_with_account, get_user_by_id, get_all_users

accounts_bp = Blueprint('accounts', __name__)


accounts_bp.add_url_rule('/users', 'create_user_with_account', create_user_with_account, methods=['POST'])
accounts_bp.add_url_rule('/users/<int:user_id>', 'get_user_by_id', get_user_by_id, methods=['GET'])
accounts_bp.add_url_rule('/users', 'get_all_users', get_all_users, methods=['GET'])
