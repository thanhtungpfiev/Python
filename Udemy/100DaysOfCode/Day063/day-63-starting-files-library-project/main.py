from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

# create the extension
db = SQLAlchemy()

# initialize the app with the extension
db.init_app(app)


# CREATE TABLE
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', all_books=all_books)


@app.get('/add')
def add_view():
    return render_template('add.html')


@app.post('/add')
def add_book():
    book_name = request.form.get('book_name')
    book_author = request.form.get('book_author')
    rating = request.form.get('rating')
    book = Books(title=book_name, author=book_author, rating=rating)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('home'))


@app.get('/edit')
def edit_view():
    book = Books.query.get_or_404(request.args.get('id'))
    return render_template('edit.html', book=book)


@app.post('/edit')
def edit_book():
    book = Books.query.get_or_404(request.form['id'])
    book.rating = request.form['rating']
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = Books.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    # Create table schema in the database. Requires application context.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
