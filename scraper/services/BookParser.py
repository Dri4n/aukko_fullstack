import sys, os, json
current_path = os.path.join(os.path.dirname(__file__), os.path.pardir)
solution_path = os.path.abspath(os.path.join(current_path, os.path.pardir))
sys.path.append(solution_path)

from data.BookContext import Session, engine, Base
from data.models.Categories import Category
from data.models.Books import Book

class BookParser:
    def __init__(self):
        # eliminamos y creamos los datos de la base de datos.
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        self.categories = []
        self.books = []

    def load_data(self):
        with open(current_path + '/data/categories.json', 'r', encoding='utf-8') as f:  
           self.categories = json.load(f)
        with open(current_path + '/data/books.json', 'r', encoding='utf-8') as f:  
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
        db_categories = self.get_db_categories()
        session = Session(bind=engine)
        session.bulk_save_objects([
            Book(
                title = book['title'],
                category_id = next(filter(lambda x: x.url == book['category_url'], db_categories), Category).id,
                thumbail_url = book['thumbail'],
                price = book['price'],
                price_tax = book['price_tax'],
                tax = book['tax'],
                stock = book['stock'],
                description = book['description'],
                upc = book['upc']
            )
            for book in self.books
        ])
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

        print(f'CATEGORIAS CARGADAS EN BD - {len(self.get_db_categories())}')
        print(f'LIBROS CARGADOS EN BD- {len(self.get_db_books())}')