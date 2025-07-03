from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base


class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True)
    loaned_to = Column(String, ForeignKey('borrowers.id'))
    loaned_from = Column(String, ForeignKey('libraries.id'))
    book = Column(String, ForeignKey('books.id'))
    borrow_date = Column(Integer)
    return_date = Column(Integer)
    due_date = Column(Integer)

    borrowers = relationship('Borrower', backref='loans')
    libraries = relationship('Library', backref='loans')
    books = relationship('Book', backref='loans')


