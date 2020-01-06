from flask import Flask

app = Flask(
  __name__
)


@app.route('/index')
def index():
  return "hehsskfnlxncsdkz"

@app.route('/truth')
def get_truth():
  return "Puns are the worst"

app.run(
   '0.0.0.0',
   port=8080
)


