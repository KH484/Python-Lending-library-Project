from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from src.base import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    genre = Column(String)
    fiction = Column(Boolean)
    title = Column(String)
    library = Column(Integer, ForeignKey('libraries.id'))
    libraries = relationship('Library', backref='books')

    def __str__(self):
        return f"{self.title} by {self.author}"



