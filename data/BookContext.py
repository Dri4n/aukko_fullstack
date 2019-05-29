from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db_path = os.path.join(os.path.dirname(__file__), 'bookscraper.db')
engine = create_engine('sqlite:///{}'.format(db_path))
Session = sessionmaker(bind=engine)
Base = declarative_base()
