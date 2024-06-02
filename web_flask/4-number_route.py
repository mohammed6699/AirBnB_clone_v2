from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes=False
@app.route("/")

def hello_world():
    return 'Hello HBNB!'

@app.route("/hbnb")
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def n_is_number(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)