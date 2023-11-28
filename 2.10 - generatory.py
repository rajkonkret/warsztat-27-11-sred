# generatory -

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # odsyłą wynik, zapamietuje pozycje gdzie skończyło


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x000001D13E78FED0>

print(next(kwa))
print(next(kwa))
print(next(kwa))
print(next(kwa))
print("Zrob cokolwiek")
lista = []
lista.append("123456")
print(lista)
print(next(kwa))  # 16
print(type(kwa))  # <class 'generator'>
# print(next(kwa))  # StopIteration
kwa2 = kwadrat2(6)
print("kwa2", next(kwa2))
print("kwa2", next(kwa2))
print("kwa2", next(kwa2))
print("kwa2", next(kwa2))  # kwa2 9
kwa3 = kwadrat2(10)
print("kwa3", next(kwa3))  # kwa3 0

lista = list(range(10))
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
