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




