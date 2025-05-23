from flask import Blueprint, jsonify
from app.db.models import get_all_users

test_bp = Blueprint('test', __name__)

@test_bp.route('/api/test-db', methods=['GET'])
def test_db():
    try:
        users = get_all_users()
        return jsonify({"success": True, "users": users})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
