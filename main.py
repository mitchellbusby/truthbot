from flask import Flask, jsonify
import random

app = Flask(
  __name__
)


@app.route('/index')
def index():
  return "hehsskfnlxncsdkz"

TRUTHS = [
  'Trams are the best',
  'Puns are the worst'
]

@app.route('/truth', methods=["GET", "POST"])
def get_truth():
  text = random.choice(TRUTHS)
  message = {
    'author': 'truthbot',
    'text': text
  }
  return jsonify(message)

app.run(
   '0.0.0.0',
   port=8080
)


