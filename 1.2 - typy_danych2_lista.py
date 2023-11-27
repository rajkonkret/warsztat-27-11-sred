# lista  - kolekcja, przechowuje dowolną ilośc danych, dowolnego typu na raz
# lista zachowuje kolejność dodawania

lista = []  # pusta lista
print(type(lista))  # <class 'list'>

# dodawanie elemntu n koncu listy
lista.append("Tomek")
lista.append("Radek")
lista.append("Zenek")
lista.append("Darek")
print(lista)  # ['Tomek', 'Radek', 'Zenek', 'Darek']

# posiada indeks
# liczone od 0

print(lista[0])  # pierwsza pozycja
print(lista[3])  # ostatni element
print(lista[-1])  # ostatni elemnt
# ['Tomek', 'Radek', 'Zenek', 'Darek']
#    0(-4)        1(-3)         2(-2)       3(-1)

print(lista[0:3])  # od indeksu 0 do 2 - zbior  prawej otwarty, 3 nie brane pod uwage
# ['Tomek', 'Radek', 'Zenek']
print(lista[0:3:2])  # ['Tomek', 'Zenek'] start:stop:krok

# zamiana elemntu na danym indeksie
lista[0] = "Radek"
print(lista)

# wstawienie elemntu pommiedzy indeksy
lista.insert(1, "Grzegorz")
print(lista)  # ['Radek', 'Grzegorz', 'Radek', 'Zenek', 'Darek']
print(len(lista))  # 5

# usunięcie elemntu (pierwszy napotkany)
lista.remove("Radek")  # ['Grzegorz', 'Radek', 'Zenek', 'Darek']
print(lista)

# usuniecie po indeksie
print(lista.pop(3))  # Darek, wypisze element, który usunął
print(lista)

# sprawdzenie indeksu elemntu
print(lista.index("Zenek"))  # 2

a = 8
b = 9
a = b
print(a)  # 9
b = 128
print(a)  # 9
lista_copy = lista  # kopia referencji listy (adresu pamieci)
print(lista_copy)  # ['Grzegorz', 'Radek', 'Zenek']
lista_copy_ok = lista.copy()  # kopia elementów listy
lista.clear()  # usunięcie wszystkich elementów
print(lista_copy)  # []
print(id(lista_copy))  # 2356439240192
print(id(lista))  # 2356439240192
print(id(lista_copy_ok))  # 2356441675072
print(lista_copy_ok)  # ['Grzegorz', 'Radek', 'Zenek']

liczby = [54, 999, 34, 22, 12.34, 876]
# liczby = [54, 999, 34, 22, 12.34, 876, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'

print(liczby)
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 876, 999]

lista_liata = [1, 2, 3, [1, 2, 3]]
print(lista_liata)  # [1, 2, 3, [1, 2, 3]]
# numpy - dedykowana do operacji na tablicach

print(liczby[0:3])  # [12.34, 22, 34]
liczby.append(4)
liczby.remove(34)
liczby.insert(1, 46)
print(liczby)  # [12.34, 46, 22, 54, 876, 999, 4]

print(lista_liata[3])  # [1, 2, 3]
print(lista_liata[3][1])  # 2

lista3 = ['a', 'b', 'c']
lista4 = ["1", "2", "3"]
lista3.extend(lista4)
print(lista3)  # ['a', 'b', 'c', '1', '2', '3']
lista5 = "definicja"
lista3.extend(lista5)
print(lista3)
# ['a', 'b', 'c', '1', '2', '3', 'd', 'e', 'f', 'i', 'n', 'i', 'c', 'j', 'a']
# rozpakowanie sekwencji

tekst = "Python"
lista_z_tekstu = list(tekst)  # -> extend()
print(lista_z_tekstu)  # ['P', 'y', 't', 'h', 'o', 'n']

lista6 = [tekst]  # append()
print(lista6)  # ['Python']

liczby = 1234  # int()
liczby3 = []
liczby3.extend(str(liczby))  # zamiana na string str()
print(liczby3)  # ['1', '2', '3', '4']

krotka = tuple(liczby3)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('1', '2', '3', '4')
