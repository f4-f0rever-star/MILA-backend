from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.progress import Progress
from app.models.favorite import Favorite
from app.models.users import User
from app.extensions import db

bp = Blueprint("user", __name__)

@bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user.to_dict()), 200

@bp.route("/progress", methods=["GET", "POST"])
@jwt_required()
def user_progresss():
    identity = get_jwt_identity()

    user = User.query.get(identity)

    if request.method == "GET":
        rows = Progress.query.filter_by(user_id = user.id).all()
        return jsonify([
            {
                "culture_id": r.culture_id,
                "topic": r.topic,
                "completed": r.completed,
                "updated_at": r.updated_at.isoformat()
            }
            for r in rows
        ]), 200
    
    if request.method == "POST":
        data = request.get_json()
        culture_id = data.get("culture_id")
        topic = data.get("topic")
        completed = data.get("completed", False)

        if not culture_id or not topic:
            return jsonify({"error": "Missing Fields"}), 400
        
        prog = Progress.query.filter_by(
            user_id = user.id,
            culture_id = culture_id,
            topic = topic
        ).first()

        if not prog:
            prog = Progress(
                user_id = user.id,
                culture_id = culture_id,
                topic = topic,
                completed = completed
            )
            db.session.add(prog)
            db.session.commit()
        else:
            prog.completed = completed
            db.session.commit()

        return jsonify({"message": "Progress Updated"}), 200
        
@bp.route("/favorites",  methods=["GET", "POST", "DELETE"])
@jwt_required()
def user_favorite():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if request.method == "GET":
        rows = Favorite.query.filter_by(user_id=user.id).all()
        return jsonify([
            {
                "id": f.id,
                "favorite_type": f.favorite_type,
                "external_id": f.external_id,
                "created_at": f.created_at.isoformat()
            }
            for f in rows
        ]), 200
    
    if request.method == "POST":
        data = request.get_json()
        t = data.get("type")
        eid = data.get("external_id")

        if not t or not eid:
            return jsonify({"error": "Missing fields"}), 400
        
        fav = Favorite(
            user_id = user.id,
            favorite_type = t,
            external_id = eid
        )
        db.session.add(fav)
        db.session.commit()
        return jsonify({"message": "Added to favorites"}), 201
    
    if request.method == "DELETE":
        fid = request.args.get("id")
        if not fid: 
            return jsonify({"error": "Missing favorite ID"}), 400
        
        fav = Favorite.query.filter_by(id=fid, user_id=user.id).first()
        if not fav:
            return jsonify({"error": "favorite not found"}), 404
        
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"message": "Removed from favorites"}), 200