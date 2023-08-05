from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9"
                     ".eyJhdWQiOiIzNjBmOGY0N2RiNWE2MDE4MTVlYWUwNDMxZGIyMmJhNSIsInN1YiI6IjY0Y2RiYTU3ODUwOTBmMDE0NDVhZDAzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1NTiFcHchbxhucKJ_rlFI22shEerqLpV-BP0f8mWJYM"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"

# create the extension
db = SQLAlchemy()

# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=True)

    # Optional: this will allow each movie object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'


class MovieAddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class MovieUpdateForm(FlaskForm):
    rating = DecimalField("Your Rating Out of 10 e.g. 7.5", places=2, validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


# new_movie = Movie( title="Phone Booth", year=2002, description="Publicist Stuart Shepard finds himself trapped in a
# phone booth, pinned down by an extortionist's " "sniper rifle. Unable to leave or receive outside help,
# Stuart's negotiation with the caller leads to " "a jaw-dropping climax.", rating=7.3, ranking=10, review="My
# favourite character was the caller.", img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg" )
#
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family ("
#                 "Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
#                 "other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieAddForm()
    if form.validate_on_submit():
        movie_title = request.form['title']
        response = requests.get(MOVIE_DB_SEARCH_URL, headers=headers, params={'query': movie_title})
        response.raise_for_status()
        data = response.json()['results']
        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieUpdateForm()
    if form.validate_on_submit():
        movie = Movie.query.get_or_404(request.args.get('id'))
        movie.rating = request.form['rating']
        movie.review = request.form['review']
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie = Movie.query.get_or_404(request.args.get('id'))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/get_movie_detail")
def get_movie_detail():
    movie_id = request.args.get('id')
    response = requests.get(f"{MOVIE_DB_INFO_URL}/{movie_id}", headers=headers, params={'language': 'en-US'})
    response.raise_for_status()
    data = response.json()
    new_movie = Movie(title=data['title'], img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
                      year=data['release_date'].split("-")[0],
                      description=data['overview'])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    # Create table schema in the database. Requires application context.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
