import sys, os, json
solution_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(solution_path)

from sqlalchemy import or_
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

from data.BookContext import Session, engine, Base
from data.models.Categories import Category
from data.models.Books import Book
Base.metadata.create_all(engine)

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route("/api/v1/categories", methods=['GET'])
def categories():
    session = Session(bind=engine)
    response = session.query(Category).all()
    session.close()
    
    data = [ob._asdict() for ob in response]
    return json.dumps(data, ensure_ascii=False)

@app.route("/api/v1/books/search", methods=['POST'])
def search_books():
    data = request.get_json()

    search_text = data.get('query')
    limit = data.get('limit')
    ascending = data.get('ascending')
    page = data.get('page')
    byColumn = data.get('byColumn')
    categoryId = data.get('categoryId')
    
    if limit is None:
        limit = 5
    if page is None or page < 1:
        page = 1

    offset = (page - 1) * limit

    session = Session(bind=engine)
    query = session.query(Book).join(Book.category)
    if categoryId is not None and int(categoryId) > 0:
        query = query.filter(Book.category_id == categoryId)
    if search_text is not None and len(search_text):
        search_text = f'%{search_text.strip()}%'
        query = query.filter(
            Book.title.like(search_text),
            Book.description.like(search_text)
        )

    response = {
        'count':  query.count(),
        'data': [ob._asdict() for ob in query.limit(limit).offset(offset).all()]
    }
    session.close()
    
    return jsonify(response)

@app.route("/api/v1/books/<book_id>/delete", methods=['DELETE'])
def delete_book(book_id):
    return book_id

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)