# dekoratory - @dekorator_nazwa
# funkcja opakowująca inna funkcję w dodatkowe własciwosci (działanie)
# zbudowane są na zasadzie funkcji wewnętrznej

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwracamy wynik działąnia funkcji dekorowanej

    return wew # zwracamy adres funkcji wewnętrznej


@dekor
def hej():
    print("Hej!!!")


hej()
# Hej!!!
# po dodaniu dekoratora @dekor
# Dekorujemy
# Hej!!!
