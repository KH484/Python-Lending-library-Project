from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from Models.book import Book
from Models.borrower import Borrower
from Models.library import Library
from Models.loan import Loan


engine = create_engine('postgresql+psycopg2://katherineheard@localhost:5432/book_loan_database', echo=True)

conn = engine.connect()

Base = declarative_base()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

pride_and_prejudice = Book(id = 1, title = "Pride and Prejudice", author = "Jane Austen", genre = "Classic", fiction = True, library= "Hogwarts")
session.add(pride_and_prejudice)
session.commit()
session.close()

Lucy = Borrower(name = "Lucy")
session.add(Lucy)

British_Library = Library(name = "British Library", address = "96 Euston Road, London, NW1 2DB")
session.add(British_Library)





