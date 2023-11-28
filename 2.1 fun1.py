# funkcje - fragment kodu, który możemy wykonać wielokrotnie w dowolnym momencie
# funkcja musi być najpierw zdefiniowana, dopiero po zdefiniowaniu może byc wykonana

a = 8
b = 9


# definicja funkcji
def dodaj():  # nie ma argumentow
    # pass # nic nie rób
    print(a + b)


# python nie wspiera przeciążania argumntów funkcji
def dodaj2(a, b):  # ma dwa obowiązkowe argumenty
    print(a + b)


def odejmowanie(a, b, c=0):  # a i b obowiązkowe, c moze byc przekazany lub nie,
    # wtedy przyjmie wartość domyślną c=0
    print(a - b - c)


def mnozenie2(a, b):
    return a, b, a * b


# wywołanie funkcji
# nazwa funkcji () - ewentualnie argumenty w nawiasach
dodaj()  # 17
dodaj2(5, 7)  # 12
odejmowanie(1, 2)  # -1
odejmowanie(1, 2, 3)  # -4  tutaj przekazane po pozycji. kolejnosc wyznacza do którego trafi
odejmowanie(b=7, c=9, a=7)  # -9 argumenty przekazane po nazwie
print(odejmowanie(1, 2, 3))  # None
print(mnozenie2(2, 6))  # (2, 6, 12)
# rozpakowac krotke do 3trzech zmiennych i ładnie wypisac f-stringiem
a, b, c = mnozenie2(5, 6)  # rozpakowanie krotki
print(f"Wynik {a} * {b} = {c}")  # Wynik 5 * 6 = 30

