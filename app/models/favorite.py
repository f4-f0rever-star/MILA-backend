from app.extensions import db

class Favorite(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    favorite_type = db.Column(db.String(20), nullable = False)
    external_id = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, default = db.func.now())