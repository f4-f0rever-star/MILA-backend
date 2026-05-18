from flask import Blueprint
from app.routes.auth import bp as auth_bp
from app.routes.cultures import bp as cultures_bp
from app.routes.quiz import bp as quiz_bp
from app.routes.user import bp as user_bp

def register_blueprint(app):
    app.register_blueprint(auth_bp, url_prefix = "/api/auth")
    app.register_blueprint(cultures_bp, url_prefix = "/api/cultures")
    app.register_blueprint(quiz_bp, url_prefix = "/api/quiz")
    app.register_blueprint(user_bp, url_prefix = "/api/user")