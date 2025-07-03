import pytest


from ...src.Models.book import Book
from ...src.Models.library import Library
from ...src.Models.borrower import Borrower

#import database

@pytest.fixture
def book():
    book = Book("Origin", "Dan Brown", "Thriller")
    return book

@pytest.fixture
def library():
    library = Library(1, "Hogwarts Library")
    library.inventory = []
    return library

@pytest.fixture
def borrower():
    borrower = Borrower(1, "Elizabeth")
    borrower.borrowed_book = []
    return borrower

def test_add_book(book, library):
    library.add_book(book)
    assert len(library.inventory) > 0





