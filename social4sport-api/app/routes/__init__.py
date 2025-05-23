from .auth import auth_bp
# from .users import users_bp
# from .matches import matches_bp
from .test import test_bp  # <-- add this

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    # app.register_blueprint(users_bp, url_prefix='/api/users')
    # app.register_blueprint(matches_bp, url_prefix='/api/matches')
    app.register_blueprint(test_bp)  # no prefix
