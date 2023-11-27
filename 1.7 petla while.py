# while - sterowana warunkiem

licznik = 0
while True:  # warunek zawsze True -> petla nieskończona
    licznik += 1  # licznik = licznik + 1
    print("Komunikat!!!")
    if licznik > 10:
        break  # przerwanie petli

print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("komuniakt2!!!")

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(int(wej))
    lista2.append(wej)

print(lista)  # [2, 3, 4]
print(lista2)  # ['1', '2', '3']
