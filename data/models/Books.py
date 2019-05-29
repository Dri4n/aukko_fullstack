from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey
from data.BookContext import Base
from data.models.Serialize import Serializable

class Book(Base, Serializable):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    category_id = Column(String, ForeignKey('categories.id'), nullable=False)
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