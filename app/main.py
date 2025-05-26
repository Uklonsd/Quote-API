from flask import Flask, jsonify, send_from_directory
import os
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from app.models import Quote


app = Flask(__name__)

engine = create_engine('sqlite:///quotes.db')
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def index():
  return send_from_directory(os.path.join(app.root_path, "static"), "index.html")


@app.route("/quote")
def quote():
    result = session.query(Quote).order_by(func.random()).first()
    return jsonify({
        "id": result.id,
        "author": result.author,
        "quote": result.quote,
        "image": result.image
    })


@app.route("/like/<int:quote_id>", methods=["POST"])
def like(quote_id):
    quote = session.get(Quote, quote_id)
    if quote:
        quote.likes += 1
        session.commit()
        return jsonify({"status": "ok", "likes": quote.likes})
    return jsonify({"status": "error", "message": "Quote not found"}), 404


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
