from flask import Flask, jsonify

app = Flask(
  __name__
)


@app.route('/index')
def index():
  return "hehsskfnlxncsdkz"

@app.route('/truth', methods=["GET", "POST"])
def get_truth():
  message = {
    'author': 'truthbot',
    'text': 'Puns are the worst'
  }
  return jsonify(message)

app.run(
   '0.0.0.0',
   port=8080
)


