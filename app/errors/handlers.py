from app.errors import errors_bp

from flask import jsonify, make_response


@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@errors_bp.app_errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal server error'}), 500)


@errors_bp.app_errorhandler(400)
def bad_request_error(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@errors_bp.app_errorhandler(401)
def unauthorized_error(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


@errors_bp.app_errorhandler(403)
def forbidden_error(error):
    return make_response(jsonify({'error': 'Forbidden'}), 403)


@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    return make_response(jsonify({'error': 'Method not allowed'}), 405)


@errors_bp.app_errorhandler(409)
def conflict_error(error):
    return make_response(jsonify({'error': 'Conflict'}), 409)
