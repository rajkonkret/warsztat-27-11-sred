# stworzenie ksiazki telefonicznej z wykorzystaniem petli while jako głownej petli programu
# dodaj kontakt, usun kontakt, wysszukaj kontakt, wyswietl kontakty

# stworzyc system zarzadzania biblioteka, ktory umozliwia dodawaie ksiazek, wypozyczanie, zwracanie
# klasa Book, Library
# obsłuzyc błedy
# dodac user ktory bedzie miał ksiazki jakie wypozyczyłł( moze miec ksiaziki z róznych bibliotek

# petle while
# wyswietlic menu
# w zaleznosci od opcji wykonac dana czynnosc
contacts = {}
while True:
    print(f"""
    1. Dodaj kontakt
    2. Usuń kontakt
    3. Wyszukaj kontakt
    4. Wyświetl liste kontaktow
    5. Koniec
""")
    try:
        odp = input("Wybierz opcję")
        if odp == "1":
            name = input("Podaj imie kontaktu")
            number = input("Podaj numer telefonu (tylko cyfry)")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierać cyfry!")
            else:
                contacts[name.lower()] = number
                print(f"Kontakt {name} został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name in contacts:
                # del contacts[name]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunięty")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "3":
            name = input("Podaj imię kontaktu do wyszukania")
            if name.lower() in contacts:

                print(f"Kontakt {name} nr telefonu: {contacts[name.lower()]} ")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "4":
            print(f"Lista kontaktów: {contacts}")
        elif odp == "5":
            break
        else:
            print("Błedny wybór z menu")
    except Exception as e:
        print("Bład", e)
