# dziedziczenie
from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # pusta lista, wspolna dla wszystkich obiektów tej klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name!r} {self.email!r}"


class Suplier(Contact):  # dziedziczymy po klasie Contact
    """
    Dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        return "suplier"


# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
class Friend(Suplier, Contact):  # kolejnosc ma znaczenie
    """
    Dziedziczy po klasie Suplier i Conatact
    """

    def __init__(self, name, email, phone):
        super().__init__(name, email)  # super() klasa wyzsza <class '__main__.Suplier'>
        self.phone = phone

    def order(self, order):
        print("To jest metoda z klasy Friend")
        super().order(order)
        Suplier.order(self, order)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name!r} {self.email!r}, +48 {self.phone!r}"


c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admin1@wp.pl")
c3 = Contact("Tomek", "admin2@wp.pl")
print(c1)  # Adam admin@wp.pl -> po dodaniu !r -> 'Adam' 'admin@wp.pl'
print(Contact.all_contacts)  # [Adam admin@wp.pl, Radek admin1@wp.pl, Tomek admin2@wp.pl]
s1 = Suplier("Tomasz", "tomasz@onet.pl")
print(s1)
print(Contact.all_contacts)
s1.order("Kawa")  # Kawa zamówiono od Tomasz
print(s1.all_contacts.search("Adam"))  # [Contact 'Adam' 'admin@wp.pl']

contact_list = ContactList()
contact_list.append(c1)
print(contact_list)  # [Contact 'Adam' 'admin@wp.pl']
print(contact_list.search("Adam"))  # [Contact 'Adam' 'admin@wp.pl']
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
f1 = Friend("Jarek", "jarek@wp.pl", "657876543")
print(f1)  # Friend 'Jarek' 'jarek@wp.pl', +48 '657876543'
f1.order("herbata")
print(f1)
pprint(f1)
pprint(Contact.all_contacts)
# [Contact 'Adam' 'admin@wp.pl',
#  Contact 'Radek' 'admin1@wp.pl',
#  Contact 'Tomek' 'admin2@wp.pl',
#  suplier,
#  Friend 'Jarek' 'jarek@wp.pl', +48 '657876543']
