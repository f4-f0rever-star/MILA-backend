from app.extensions import db
from datetime import datetime

class Progress(db.Model):
    __tablename__ = "progress"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    culture_id = db.Column(db.String(50), nullable = False)
    topic = db.Column(db.String(50), nullable = False)
    completed = db.Column(db.Boolean, default = False)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)