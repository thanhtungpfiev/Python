from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        temp_str = function()
        return f"<b>{temp_str}</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        temp_str = function()
        return f"<em>{temp_str}</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        temp_str = function()
        return f"<u>{temp_str}</u>"

    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
