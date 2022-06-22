from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.wrappers import response
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = os.environ['MOVIE_DB_API_KEY']

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.String(4),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.String(1),nullable=True)
    review = db.Column(db.String(200),nullable=True)
    img_url = db.Column(db.String(500),nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()

class UpdateForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    title = StringField(label='Enter Movie Name', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')

db.create_all()

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    #This line loops through all the movies
    for i in range(len(all_movies)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html",movies=all_movies)


@app.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience 
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY})
        response.raise_for_status()
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))


@app.route('/update', methods=['GET','POST'])
def update():
    form = UpdateForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        if form.rating.data:
            movie.rating = float(form.rating.data)
        if form.review.data:
            movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template("edit.html", movie=movie, form=form) 


@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))





if __name__ == '__main__':
    app.run(debug=True)




# id 
# title - Drive
# year 2011
# description -   A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama.
# rating 7.5 
# ranking = 1
# review Loved it!
# img_url = https://www.shortlist.com/media/images/2019/05/the-30-coolest-alternative-movie-posters-ever-2-1556670563-K61a-column-width-inline.jpg