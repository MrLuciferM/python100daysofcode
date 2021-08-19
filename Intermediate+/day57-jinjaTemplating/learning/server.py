from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = date.today().year
    return render_template('index.html',num=random_number,year=current_year)

@app.route('/guess/<name>')
def guess_details(name):
    GENDERIZE_ENDPOINT = 'https://api.genderize.io/'
    AGIFY_ENDPOINT='https://api.agify.io/'
    parameters = {
        'name':name
    }
    data = requests.get(url=GENDERIZE_ENDPOINT,params=parameters)
    data.raise_for_status()
    gender = data.json()['gender']
    
    data = requests.get(url=AGIFY_ENDPOINT,params=parameters)
    data.raise_for_status()
    age=data.json()['age']

    return render_template('guesser.html',name=name,gender=gender,age=age)


@app.route('/blog')
def blogs():
    BLOGS_ENDPOINT = 'https://api.npoint.io/0fdc688b3ef82bbd2567'
    response = requests.get(url=BLOGS_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    return render_template('blog.html',posts=data)

if __name__ == '__main__':
    app.run(debug=True)