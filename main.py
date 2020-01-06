from flask import Flask

app = Flask(
  __name__
)


@app.route('/index')
def index():
  return "hehsskfnlxncsdkz"


app.run()


