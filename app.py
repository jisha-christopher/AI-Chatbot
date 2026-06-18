from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from chatbot import get_response
from database import chat_logs

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html"
    )

@app.route("/chat", methods=["POST"])
def chat():

    msg = request.json["message"]

    reply = get_response(msg)

    chat_logs.insert_one(
        {
            "user": msg,
            "bot": reply
        }
    )

    return jsonify(
        {
            "response": reply
        }
    )

if __name__ == "__main__":
    app.run(
        debug=True
    )