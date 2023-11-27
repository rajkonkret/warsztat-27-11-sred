# krotka - kolekcja niezmienna
# zmienna niezmienna
tupla = "Radek"
print(type(tupla))  # <class 'str'>
tupla1 = ("Radek")
print(type(tupla1))  # <class 'str'>
tupla2 = "Radek",
print(type(tupla2))  # <class 'tuple'>
tupla3 = ("Radek",)
print(type(tupla3))
print(tupla3)  # ('Radek',)
tupla4 = "Tomek", "Radek", "Zenek", "Magda"
print(type(tupla4))
print(tupla4)  # ('Tomek', 'Radek', 'Zenek', 'Magda')

tupla5 = 44, 34, 22.43, 11, 200
print(tupla4[0])  # Tomek

print(tupla4.count("Tomek"))  # 1
print(tupla4.index("Radek"))  # 1

# rozpakowanie tupli
a, b = 1, 2  # o prawej stronie mamy tuple
print(a)
print(b)

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * worek na pozostałe dane
print(a)
print(type(a))
print(b)  # [2, 3]
print(type(b))  # <class 'list'>

# rozpakowac tupla4 na trzy zmienne w mozliwych wariantach
imie1, imie2, *imie3 = tupla4  # ('Tomek', 'Radek', 'Zenek', 'Magda')
print(imie1)
print(imie2)
print(imie3)
# Tomek
# Radek
# ['Zenek', 'Magda']
imie1, *imie2, imie3 = tupla4  # ('Tomek', 'Radek', 'Zenek', 'Magda')
print(imie1, imie2, imie3)  # Tomek ['Radek', 'Zenek'] Magda

lista_krotka = list(tupla4)
print(type(lista_krotka))
print(lista_krotka)  # ['Tomek', 'Radek', 'Zenek', 'Magda']
