from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.base import Base


class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, unique=True, primary_key=True)
    borrow_date = Column(Integer)
    return_date = Column(Integer)
    due_date = Column(Integer)

    loaned_to = Column(Integer, ForeignKey('borrowers.id'))
    loaned_from = Column(Integer, ForeignKey('libraries.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    borrower = relationship('Borrower', backref='loans')
    library = relationship('Library', backref='loans')
    book = relationship('Book', backref='loans')


