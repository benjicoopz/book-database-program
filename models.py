from sqlalchemy import create_engine, Column, Integer, String, Date
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = sqlalchemy.orm.declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column('Published', Date)
    price = Column('Price', Integer)

    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Published: {self.published_date} Price: {self.price}'
#create a database
#books.db
#create a model
# title, author, date published, price