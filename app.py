from models import (Base, session, Book, engine)
# import models
# main menu - add, search, analysis, exit, view
# add books to db
# edit books
# delete books
# search func
# data cleaning func
# loop runs program


if __name__ == '__main__':
    Base.metadata.create_all(engine)
