import sys, os
sys.path.append(os.path.abspath(os.path.join('../../', '')))

from context.BookContext import Session, engine, Base
from context.models.Categories import Category
Base.metadata.create_all(engine)
movies = session.query(Category).all()
print(movies)

session.close()