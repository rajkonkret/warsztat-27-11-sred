# dziedziczenie

class Contact:
    all_contacts = []  # pusta lista, wspolna dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.name!r} {self.email!r}"


class Suplier(Contact):  # dziedziczymy po klasie Contact
    """
    Dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admin1@wp.pl")
c3 = Contact("Tomek", "admin2@wp.pl")
print(c1)  # Adam admin@wp.pl -> po dodaniu !r -> 'Adam' 'admin@wp.pl'
print(Contact.all_contacts)  # [Adam admin@wp.pl, Radek admin1@wp.pl, Tomek admin2@wp.pl]
s1 = Suplier("Tomasz", "tomasz@onet.pl")
print(s1)
print(Contact.all_contacts)
s1.order("Kawa")  # Kawa zamówiono od Tomasz


# klasa pojazd i klasa samochod dziedziczaca po niej

class Pojazd:
    """
    klasa pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor


class Samochod(Pojazd):
    """
    Klasa samochod
    """
