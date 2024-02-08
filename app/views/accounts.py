from flask import Blueprint
from app.controllers.accounts import get_all_users, get_user_by_id, create_user, update_user, delete_user

# Create a Blueprint for the accounts-related endpoints
accounts_blueprint = Blueprint('accounts', __name__)


# Define routes for the endpoints
accounts_blueprint.route('/users', methods=['GET'])(get_all_users)
accounts_blueprint.route('/users/<int:user_id>', methods=['GET'])(get_user_by_id)
accounts_blueprint.route('/users', methods=['POST'])(create_user)
accounts_blueprint.route('/users/<int:user_id>', methods=['PUT'])(update_user)
accounts_blueprint.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
