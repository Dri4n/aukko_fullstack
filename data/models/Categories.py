import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from data.BookContext import Base
from data.models.Serialize import Serializable

class Category(Base, Serializable):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False, unique=True)
    books = relationship("Book", backref="user", lazy='subquery')
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    def __init__(self, name, url):
        self.name = name
        self.url = url