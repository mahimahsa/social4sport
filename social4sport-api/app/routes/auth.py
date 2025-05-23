from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from app.db.models import get_or_create_user_by_google_id

import os

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/google-login', methods=['POST'])
def google_login():

    try:
        # Validate the Google ID token
        print(" /google-login endpoint hit")

        client_id = ""
        print("GOOGLE_CLIENT_ID found:", client_id)

        data = request.get_json()
        token = data.get('token')
        print("Token received:", token[:20] + "...")

        idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), client_id)
        print("Verified Google user:", idinfo.get('email'))


        google_id = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name')
        picture = idinfo.get('picture')

        # DB: create or get user
        user_id = get_or_create_user_by_google_id(google_id, email, name, picture)

        # Issue JWT token
        access_token = create_access_token(identity=user_id)
        return jsonify(access_token=access_token)

    except Exception as e:
        print("❌ Login error:", e)
        return jsonify({"error": str(e)}), 400
