from flask import Blueprint, request, jsonify
from app.services.cuisine import get_meals_by_country
from app.services.countries import get_countries
from app.services.art import get_art_by_country
from app.services.history import get_history
from app.services.traditions import get_heritage_by_country

bp = Blueprint("cultures", __name__)

@bp.route("/", methods=["GET"])
def list_cultures():
    cultures = [
        {"id": "kenya", "name": "Kenya", "continent": "Africa"},
        {"id": "japan", "name": "Japan", "continent": "Asia"},
        {"id": "greece", "name": "Greece", "continent": "Europe"},
        {"id": "mexico", "name": "Mexico", "continent": "America"}
    ]
    return jsonify(cultures), 200

@bp.route("/<culture_id>", methods=["GET"])
def get_culture(culture_id):

    id = culture_id.strip().lower()

    food_data = get_meals_by_country(id)
    country_data = get_countries(id)
    art_data = get_art_by_country(id)
    history_data = get_history(id)
    traditions_data = get_heritage_by_country(id)

    return jsonify({
        "culture_id": culture_id,
        "name": "Culture",
        "food": food_data,
        "country": country_data,
        "art": art_data,
        "history": history_data,
        "traditions": traditions_data
    }), 200