from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from data.BookContext import Base
from data.models.Serialize import Serializable

class Category(Base, Serializable):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False, unique=True)
    book = relationship("Book")

    def __init__(self, name, url):
        self.name = name
        self.url = url