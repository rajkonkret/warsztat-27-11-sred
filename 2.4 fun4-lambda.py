# lambda - skrócony zapis funkcji
# mozliwosc zadeklarowania w miejscu uzycia

def liczymy(x, y):
    return x * y


print(liczymy(5, 9))

liczymy2 = lambda x, y: x * y  # lambda z założenia zwraca wynik (return)
print(liczymy2(7, 6))  # 42

lista = [1, 2, 3, 4, 5, 6, 7, 20, 55, 100, 123]

# przemnozenie kazdego elemntu przez 2 i stworzenie nowej listy
print([i * 2 for i in lista])  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
lista2 = []
for i in lista:
    lista2.append(i * 2)
print(lista2)  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]


def zmien(x):
    return x * 2


# map() - mapowanie, pobiera kolejne elementy kolekcji, wykonuje na nich działanie podane w postaci funkcji
print(f"Użycie map() {list(map(zmien, lista))}")  # Użycie map() [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
# Uzycie labdy jako funkcji zdefiniowanej w miejscu wykonania (funkcja anonimowa)
print(f"Użycie map() {list(map(lambda x: x * 2, lista))}")  # Użycie map() [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
# filter() - filtruje i zwraca spełniajace warunek zadany funkcja
print(f"Użycie filter() {list(filter(lambda x: x > 8, lista))}")  # Użycie filter() [20, 55, 100, 123]
# x >3 i x < 30
print(f"Użycie filter() {list(filter(lambda x: 3 < x < 30, lista))}")  # Użycie filter() [4, 5, 6, 7, 20]
# uzyc map lub filter i wyfiltrowac parzyste
# przemapowac na kwadrat liczby(potega 2)
print(f"Parzyste {list(filter(lambda x: x % 2 == 0, lista))}")  # % reszta z dzielenia
# Parzyste [2, 4, 6, 20, 100]
print(f"Kwadrat {list(map(lambda x: x ** 2, lista))}")
# Kwadrat [1, 4, 9, 16, 25, 36, 49, 400, 3025, 10000, 15129]

r0 = {"miasto": "Kielce"}
r1 = {"miasto": "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
print(r1['ZIP'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

d_zip = lambda row: row.setdefault('ZIP', "00-000")
print(d_zip(r0))
print(d_zip(r1))
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}
# 11:30
