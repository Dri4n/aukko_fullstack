import sys, os, json
sys.path.append(os.path.abspath(os.path.join('../', '')))

from data.BookContext import Session, engine, Base
from data.models.Categories import Category
from data.models.Books import Book
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

class BookParser:
    def __init__(self):
        self.categories = []
        self.books = []

    def load_data(self):
        with open('data/categories.json', 'r', encoding='utf-8') as f:  
           self.categories = json.load(f)
        with open('data/books.json', 'r', encoding='utf-8') as f:  
           self.books = json.load(f)

    def save_categories(self):
        session = Session(bind=engine)
        session.bulk_save_objects(
            [
                Category(
                    name = category['name'],
                    url= category['url'],
                )
                for category in self.categories
            ]
        )
        session.commit()

    def get_db_categories(self):
        session = Session(bind=engine)
        categories = session.query(Category).all()
        session.close()
        return categories

    def save_books(self):
        session = Session(bind=engine)
        session.bulk_save_objects(
            [
                Book(
                    title= book['title'],
                    category_id = 1,
                    thumbail_url = book['thumbail'],
                    price = book['price'],
                    stock = book['stock'],
                    description = book['description'],
                    upc = book['upc']
                )
                for book in self.books
            ]
        )
        session.commit()
    
    def get_db_books(self):
        session = Session(bind=engine)
        books = session.query(Book).all()
        session.close()
        return books

    def run(self):
        self.load_data()
        self.save_categories()
        self.save_books()

        print(f'{len(self.get_db_categories())}')
        print(f'{len(self.get_db_books())}')