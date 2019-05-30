import datetime
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from data.BookContext import Base
from data.models.Serialize import Serializable
from data.models.Categories import Category

class Book(Base, Serializable):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    thumbail_url = Column(String(255), nullable=False)
    price = Column(String(30), nullable=False)
    price_tax = Column(String(30), nullable=False)
    tax = Column(String(30), nullable=False)
    stock = Column(Boolean, nullable=False)
    description = Column(String(2000), nullable=True)
    upc = Column(String(20))
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    category = relationship(Category, primaryjoin=category_id == Category.id)

    def __init__ (
        self, 
        title, 
        category_id, 
        thumbail_url, 
        price,
        price_tax,
        tax,
        stock, 
        description, 
        upc
    ):
        self.title = title
        self.category_id = category_id
        self.thumbail_url = thumbail_url
        self.price = price
        self.price_tax = price_tax
        self.tax = tax
        self.stock = stock
        self.description = description
        self.upc = upc