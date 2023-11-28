# stworzeniu raportu , przetworzeniu danych, dane generewoane generatorem.
# wykorzystamy dekorator do pomiaru czasu operacji (time)

import time


def monitor_wydajnosci(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Funkcja wykonana w czasie {end - start} sekund")
        return result

    return wrapper


# generator danych
def generator_danych(dane):
    for element in dane:
        yield element


def przetworz_dane(dane):
    przetworzone_dane = [element for element in dane if element % 2 == 0]
    return przetworzone_dane


@monitor_wydajnosci
def stworz_raport(dane):
    for element in generator_danych(dane):
        print(f"Raport dla elementu: {element}")
        # pass


dane = range(100_000)
prz_dane = przetworz_dane(dane)
stworz_raport(prz_dane)
