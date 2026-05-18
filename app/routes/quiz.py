from flask import Blueprint, request, jsonify
from app.models.quiz import Quizzes
from app.extensions import db

bp = Blueprint("quiz", __name__)

@bp.route("/", methods=["GET"])
def get_quiz():
    culture_id = request.args.get("culture_id")
    query = Quizzes.query
    if culture_id:
        query = query.filter_by(culture_id = culture_id)

    questions = query.all()
    return jsonify([
        {
            "id": q.id,
            "culture_id": q.culture_id,
            "question": q.question,
            "options": q.options,
            "difficulty": q.difficulty
        }
        for q in questions
    ]), 200

@bp.route("/submit", methods=["POST"])
def submit_answer():
    data = request.get_json()
    qid = data.get("question_id")
    selected_index = data.get("selected_index")
    if q.correct_index == selected_index:
        correct = True
    else:
        correct = False

    if qid is None or selected_index is None:
        return jsonify({"error": "Missing Answer"}), 400
    
    q = Quizzes.query.get(qid)

    if not q:
        return jsonify({"error": "Question not found"}), 404
    
    correct = q.correct.index == selected_index
    return jsonify({
        "question_id": qid,
        "correct": correct,
        "correct_index": q.correct_index
    }), 200