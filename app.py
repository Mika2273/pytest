from flask import Flask, request

appflask = Flask(__name__)

@appflask.route("/")
def hello_world():
    greeding = get_hello()
    return greeding
    # return "<p>Hello, World!</p>"

@appflask.route("/other")
def hello_other():
    page = request.args.get('page', default = 1, type = int)
    return f"<p>Hello, Other!</p><p>Page : {page}</p>"


@appflask.route("/exp")
def exp():
    value = int(request.args.get('value'))
    return f"<p>Exposant 2 de {value} : {pow(value, 2)}</p>"

def get_hello():
  return '<p>Hello, World!</p>'
