import sys, os, json
solution_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(solution_path)

from flask import Flask
from flask_restful import Resource, Api

from data.BookContext import Session, engine, Base
from data.models.Categories import Category
from data.models.Books import Book
Base.metadata.create_all(engine)

app = Flask(__name__)
api = Api(app)

@app.route("/categories", methods=['GET'])
def categories():
    session = Session(bind=engine)
    response = session.query(Category).all()
    session.close()
    
    data = [ob._asdict() for ob in response]
    return json.dumps([data], ensure_ascii=False)

@app.route("/books/search", methods=['POST'])
def search_books():
    session = Session(bind=engine)
    response = session.query(Book).all()
    session.close()
    
    data = [ob._asdict() for ob in response]
    return json.dumps([data], ensure_ascii=False)

@app.route("/books/<book_id>/delete", methods=['DELETE'])
def delete_book(book_id):
    return book_id

if __name__ == '__main__':
    app.run(debug=True)