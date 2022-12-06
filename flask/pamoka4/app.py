import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(150))
    title = db.Column(db.String(300))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))

    def __init__(self, author, title, publisher_id):
        self.author = author
        self.title = title
        self.publisher_id = publisher_id

    def __repr__(self):
        return self.title


helper_table = db.Table("helper", 
                        db.Column("book_id", db.Integer, db.Foreign("books.id")),
                        db.Column("author_id", db.Integer, db.ForeignKey("authors.id")))

class Publisher(db.Model):

    __tablename__ = "publishers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    books = db.relationship('Book', backref='publisher')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class Author(db.Model):

    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(300))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.fname} {self.lname}'

# @app.route('/')
# def database_():
#     db.create_all()
#     return '.db sukurta'

# if __name__ == "__main__":
#     # app.run(host='127.0.0.1', port=8000, debug=True)
#     with app.app_context():
#         # book1 = Book("Biliunas", "Kliudziau", 1)
#         # book2 = Book("Zemaite", "Marti", 1)
#         # book3 = Book("Mazvydas", "Katekizmas", 2)


#         # db.session.add_all([book1, book2, book3])
#         # db.session.commit()
#         books = Book.query.all()
#         print(books)

