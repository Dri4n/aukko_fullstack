from sqlalchemy import Column, String, Integer, Date
from data.BookContext import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    

    def __init__(self, name, url):
        self.name = name
        self.url = url