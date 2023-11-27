# słownik - para klucz -> wartość
# json -> {"name" : "Radek"}
# słownik: {'name':'Radek'}
# klucze nie moga sie powtarzać

slownik = {}  # pusty słownik
print(slownik)  # {}
print(type(slownik))  # <class 'dict'>

# do słownika, można dodawac pary
slownik['imie'] = 'Radek'
print(slownik)  # {'imie': 'Radek'}
slownik.update({'wiek': 39})
print(slownik)  # {'imie': 'Radek', 'wiek': 39}

# wyswietlenie elemntu po indeksie(po kluczu)
print(slownik['imie'])  # Radek

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 39])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

slownik2 = {"name": "Tomek"}
print(slownik2.items())  # dict_items([('name', 'Tomek')])

# print(slownik['age'])  # KeyError: 'age'
print(slownik.get('age', "domyslny"))  # domyslny
print(slownik.get('age', "Nie ma takiego klucza"))  # Nie ma takiego klucza
