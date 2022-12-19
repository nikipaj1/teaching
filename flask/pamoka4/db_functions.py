import app
from app import db, Book, Publisher

# app.app_context()

if __name__ == "__main__":
    # pub1 = Publisher("Baltos Lankos")
    # pub2 = Publisher("Alma Littera")


    book1 = Book("Biliunas", "Kliudziau", 1)
    book2 = Book("Zemaite", "Marti", 1)
    book3 = Book("Mazvydas", "Katekizmas", 2)


    db.session.add_all([book1, book2, book3])
    db.session.commit()