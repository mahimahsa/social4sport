from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object('app.config.Config')

    jwt.init_app(app)

    from app.routes import register_blueprints
    register_blueprints(app)

    return app
