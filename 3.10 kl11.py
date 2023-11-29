import pickle
from kl10 import Person

with open("dane.pickle", 'rb') as file:
    p = pickle.load(file)

print("---------")
print(p)  # [Person(first_name='Maciek', last_name='Nowak', id=1),
# Person(first_name='Tomek', last_name='Kowalski', id='2')]
print(type(p))  # <class 'list'>
print(p[0])

# wypisac elemnty z tej listy w postaci id, lastname, firstname
for person in p:
    print(f"id={person.id}, first name={person.first_name}, last name {person.last_name}")
    person.greet()
# id=1, first name=Maciek, last name Nowak
# id=2, first name=Tomek, last name Kowalski
