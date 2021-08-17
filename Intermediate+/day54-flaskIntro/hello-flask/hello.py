from flask import Flask

app = Flask(__name__)

# route decorator

# home
@app.route('/')
def hello_flask():
    return 'Hello Flask'

# bye route
@app.route('/bye')
def good_bye():
    return 'Byebye'

if __name__ == '__main__':
    app.run()
