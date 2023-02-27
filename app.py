import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(30), nullable=False)

@app.route("/reviews/<int:item_id>", methods=["GET", "POST"])
def reviews(item_id=None):

    if request.method == "GET":
        reviews = Review.query.filter_by(item_id=item_id).all()
        reviews_list = [{
            "id": review.id,
            "item_id": review.case_id,
            "review": review.review,
            "username": review.username,
        } for review in reviews]
        return jsonify(reviews_list)