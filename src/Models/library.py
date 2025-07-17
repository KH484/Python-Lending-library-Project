from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.base import Base


class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

# add the method to add a book to the library using the new foreign key references
# add a method to remove a book from the library

# as an example of how to reference a foreign key etc.
#     def total_loan_amount(self):
#         return sum(loan.amount for loan in self.loans)
