# stworzyc system zarzadzania biblioteka, ktory umozliwia dodawaie ksiazek, wypozyczanie, zwracanie
# klasa Book, Library
# obsłuzyc błedy
# dodac user ktory bedzie miał ksiazki jakie wypozyczyłł( moze miec ksiaziki z róznych bibliotek

class Book:
    # autor, tytuł, isbn
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author}, Tytuł: {self.title}, ISBN: {self.isbn}"


# dodaj_ksiazke
# wypozycz ksiązke
# zwróc ksiazke
# dostepne ksiaki
# wypozyczone ksiazki
# przechowywac w liscie
# wypozyczone ksiazki
# dostepne ksiazki
class Library:

    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book):
        self.dostepne_ksiazki.append(book)

    def fun_dostepne_ksiazki(self):
        return self.dostepne_ksiazki

    def fun_wypozycz_ksiazke(self, isbn):
        # usunac z dostepne
        # dodac do wypozyczonych
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book
        return Exception("Nie ma takiej ksiązki")

    def fun_zwroc_ksiazke(self, isbn):
        # usunac z wypozyczone
        # dodac do dostepne
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.append(book)
                self.wypozyczone_ksiazki.remove(book)
                return True
        return Exception("Ksiązka nie z naszej biblioteki")

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki


biblioteka = Library()
# biblioteka.fun_dodaj_ksiazke(Book("Programowanie w Pythonie", "Jan Kowalski", "1234567890"))
# biblioteka.fun_dodaj_ksiazke(Book("Programowanie w Pythonie cz. 2", "Jan Kowalski", "1234567891"))
# print(biblioteka.dostepne_ksiazki)  # [Author: Jan Kowalski, Tytuł: Programowanie w Pythonie, ISBN: 1234567890]
# []
# print(biblioteka.wypozyczone_ksiazki)  #
#
# print(biblioteka.fun_wypozycz_ksiazke("1234567890"))
# # Author: Jan Kowalski, Tytuł: Programowanie w Pythonie, ISBN: 1234567890
# print(biblioteka.dostepne_ksiazki)
# print(biblioteka.wypozyczone_ksiazki)
# # [Author: Jan Kowalski, Tytuł: Programowanie w Pythonie cz. 2, ISBN: 1234567891]
# # [Author: Jan Kowalski, Tytuł: Programowanie w Pythonie, ISBN: 1234567890]

while True:
    print(f"""1. Dodaj ksiązke
2. Wypożycz ksiązkę
3. Pokaz dostępne
5. Koniec
""")
    odp = input("Podaj opcje")
    if odp == "1":
        autor = input("Podaj autora")
        tytul = input("Podaj tytuł")
        isbn = input("Podaj numer ISBN")
        biblioteka.fun_dodaj_ksiazke(Book(tytul, autor, isbn))
        print("Ksiązka zostałą dodana")
    elif odp == "3":
        print(f"dostępne ksiązki {biblioteka.fun_dostepne_ksiazki()}")
    elif odp == "5":
        break
# dodac uzytkownika
# 13:30
