from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///moja_baza_danych.db")
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship('Book', back_populates='publisher')


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates='books')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# new_author = Author(name='Jan Kowalski')
# new_publisher = Publisher(name='Wydawnictwo Pruszyński')
# new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)
#
# print(new_book)  # <__main__.Book object at 0x00000162AFA37910>
# session.add_all(
#     [new_author, new_publisher, new_book]
# )

session.commit()

authors = session.query(Author).all()
print(authors)
for author in authors:
    print(f"Author: {author.name}")
    for b in author.books:
        print(f"Ksiązka {b.title}, Wydawca {b.publisher.name}")
# Author: Jan Kowalski
# Ksiązka Pan Tadeusz, Wydawca Wydawnictwo Pruszyński
# Author: Jan Kowalski
# Ksiązka Pan Tadeusz, Wydawca Wydawnictwo Pruszyński

publishers = session.query(Publisher).all()
print("-----------------")
for p in publishers:
    print(f"Wydawca {p.name}")
    for b in p.books:
        print(f"Ksiąka {b.title}",
              f"Autor: {b.author.name}")
# -----------------
# Wydawca Wydawnictwo Pruszyński
# Ksiąka Pan Tadeusz Autor: Jan Kowalski
# Wydawca Wydawnictwo Pruszyński
# Ksiąka Pan Tadeusz Autor: Jan Kowalski
# ctrl / - komentarz

