from flask import Blueprint, request, jsonify
from app.models.users import User
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token

bp = Blueprint("auth", __name__)

@bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if not data or not data.get("username" or not data.get("email")) or not data.get("password"):
        return jsonify({"error": "Missing Details"}), 400
    
    if User.query.filter_by(username = data["username"]).first():
        return jsonify({"error": "Username already exists"}), 409
    if User.query.filter_by(email = data["email"]).first():
        return jsonify({"error": "Email already exists"}), 409
    
    user = User(
        username = data["username"], 
        email = data["email"])
    user.password(data["password"])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user": user.to_dict()}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing Details"})
    
    user = User.query.filter_by(username = data["username"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user.id))
    return jsonify ({"access_token": token, "user": user.to_dict()}), 200