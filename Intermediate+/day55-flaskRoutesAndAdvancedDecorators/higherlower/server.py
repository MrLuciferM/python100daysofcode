from flask import Flask
from random import randint

NUMBER = randint(0, 9)
app = Flask(__name__)


def make_h1(function):
    def wrapper():
        return f'<h1>{function()}</h1>'
    return wrapper


@app.route('/')
def home():
    return '<h1 style="color: pink">Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="homegif" />'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > NUMBER:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < NUMBER:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
