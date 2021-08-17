from flask import Flask

app = Flask(__name__)

# h1 decorator

def make_h1(function):
    def add_h1():
        return f"<h1>{function()}</h1>"
    return add_h1

# route decorator
# home
@app.route('/')
def hello_flask():
    return '<h1>Hello Flask</h1>' \
        '<img src="https://images-ext-1.discordapp.net/external/D5zgbFKqpbpt_6q3WSrJMYqsnPOXDcCJ6sB15Se_mIc/%3Fv%3D1/https/cdn.discordapp.com/emojis/826032082961563669.gif" alt="image-here">'

# route with variables


@app.route('/bye/<name>')
def good_bye(name):
    return f'Byebye {name}'

# other datatypes in routes


@app.route('/<int:number>')
def print_number(number):
    return f'number {number}'


@app.route('/something')
@make_h1
def something():
    return "something something"


if __name__ == '__main__':
    app.run(debug=True)
