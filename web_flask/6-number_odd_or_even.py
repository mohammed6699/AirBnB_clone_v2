#!/usr/bin/python3
from flask import Flask, render_template

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

@app.route('/number_template/<int:n>')
def html_tempelate(n):
    return render_template("5-number.html", pagetittle="HBNB", number=n)
@app.route('/number_odd_or_even/<int:n>')
def is_odd_even(n):
    even_or_odd = "even" if n % 2 == 0 else "odd"
    values ={
        "number": n,
        "even_or_odd": even_or_odd
    }
    return render_template("6-number_odd_or_even.html", values = values)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
