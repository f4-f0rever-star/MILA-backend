from app.extensions import db

class Quizzes(db.Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key = True)
    culture_id = db.Column(db.String(50), nullable = False)
    question = db.Column(db.Text, nullable = False)
    options = db.Column(db.JSON, nullable = False)
    correct_index = db.Column(db.Integer, nullable = False)
    difficulty = db.Column(db.String(10), default = "easy")