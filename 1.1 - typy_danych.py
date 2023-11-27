print("Radek")
# 11:00
# 2 x shift - podręczna wyszukiwarka
print(type("Radek"))  # <class 'str'>
# typ str - typ znakowy - teksty
print(39)
print(type(39))  # <class 'int'> liczby całkowite
print("93")
print(type("93"))  # <class 'str'>
print("93" + "39")  # konkatenacja - łączenie stringów
print(93 + 39)
# PEP8  ctr alt l - dostosowanie kodu do PEP8
# 9339
# 132
print(5 * "93")  # 9393939393
# pudełko - mozna wrzucic co chcemy,
# nie musimy okreslac typu
# w kazdej chwili możemy wrzucic inny typ danych
wiek = "Radek"
print(wiek)  # Radek
print(type(wiek))  # <class 'str'>
wiek: int = 39  # tylko podpowiedź (hint), nie sprawdza typu
print(type(wiek))  # <class 'int'>
print(wiek)
wiek = "Radek"
print(wiek)  # Radek
# silne typowanie
# print(14 + "23")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sam nie zmienia typu, musimy jawnie zamienic typ
print(int("14") + 23)  # 37 int() - rzutowanie na typ całkowity
# print(int("") + 29)  # ValueError: invalid literal for int() with base 10: ''
print(5 * "Radek")  # RadekRadekRadekRadekRadek

wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - liczby zmiennoprzecinkowe
print(type(temp))
temp2 = 36, 6
print(type(temp2))  # <class 'tuple'> to nie jest liczba

print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# float - w postaci wykłądniczej n * 2 ^ x
# bład zaokrąglenia
# decimal - np.: do liczenia pieniedzy, operacje wolniejsze

print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # 0.023232822540781017 -> float
print(wiek // rok)  # 0 - czesc całkowita z dzielenia
print(wiek % rok)  # modulo, reszta z dzielenia
# 47 % 2023 = 0 całych i 47 reszty
print(5 % 2)  # reszta 0 lub 1

print(wiek ** rok)
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0
# ctrl d - powielenie linii w ktorej stoi kursor

print("Radek")
print('Radek')

print(wiek, rok)  # 47 2023
"""
   Prints the values to a stream, or to sys.stdout by default.

     sep
       string inserted between values, default a space.
     end
       string appended after the last value, default a newline.
     file
       a file-like object (stream); defaults to the current sys.stdout.
     flush
       whether to forcibly flush the stream.
   """
print(wiek, rok, sep=";")  # 47;2023
print(wiek, rok, sep=";", end="")  # 47;2023Radek
print("Radek")
print("Kolejna linia")  # Kolejna linia

imie = "Radek"
print("Twoje imie %s" % 39.7)
# Twoje imie 39.7
# weryfikuje typ
# %s - stringa
# %i - inta
# print("Twoje imie %i" % imie)  # TypeError: %i format: a real number is required, not str

print("Twoje imie {}".format(imie))  # Twoje imie Radek
print(f"Sprawdzam zmienna temp {temp} i wiek {wiek}")  # f-stringi - sformatowane stringi
# Sprawdzam zmienna temp 36.6 i wiek 47

wersja = 3.900001  # float
print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4
# zaokrągla przy wyswietlaniu

print(f"""
Tekst wielolinijkowy
    kolejna linijka
""")
# Tekst wielolinijkowy
#     kolejna linijka
print(f"dodaj tabulator,\n\t w kolejnej linii\b")
# dodaj tabulator,
# 	 w kolejnej lini
# \n - nowa linia
# \t - tabulator
# \b - backspace

imie = "Radek Radek"
print(type(imie))  # <class 'str'>

imie.lower()  # zamiana na małe literki
""" Return a copy of the string converted to lowercase. """
print(imie.lower())  # radek radek
imie2 = imie.lower()
print(imie2)  # radek radek
print(imie)  # Radek Radek
# upper, capitalize, title
print(imie.capitalize())  # Radek radek
print(imie.upper())
print(imie.title())  # Radek Radek

print(imie.replace(" ", "a"))  # RadekaRadek
print(imie.count("a"))  # 2
print(imie)
print(len(imie))  # długoc sekwencji
# tekst posiada indeks
# indeksowane od 0
print(imie[0])  # wypisanie literki o indeksie 0 R - pierwsza literka
print(imie.count("a", 0, 3))  # 1 jedna literka "a", bierze: Rad 0,1,2 - indeks 3 juz nie brany
print(imie.count("e", 0, 3))  # 0, bierze: Rad 0,1,2 - indeks 3 juz nie brany

liczba = 456765345890
print(f"Nasza duża liczba {liczba}")  # Nasza duża liczba 456765345890
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,765,345,890
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 456.765.345.890
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 456.765.345.890

liczba2 = 1111112.768
print(f"Nasza duża liczba {liczba2:,}".replace(",", " "))  # Nasza duża liczba 1 111 112.768
















