from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from data.BookContext import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category_id = Column(String, ForeignKey('categories.id'))
    thumbail_url = Column(String)
    price = Column(String)
    stock = Column(Boolean)
    description = Column(String)
    upc = Column(String)

    def __init__ (
        self, 
        title, 
        category_id, 
        thumbail_url, 
        price, 
        stock, 
        description, 
        upc
    ):
        self.title = title
        self.category_id = category_id
        self.thumbail_url = thumbail_url
        self.price = price
        self.stock = stock
        self.description = description
        self.upc = upc