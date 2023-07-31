from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

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


with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add_view(new_book)
    db.session.commit()

# if __name__ == "__main__":
#     app.run(debug=True)
