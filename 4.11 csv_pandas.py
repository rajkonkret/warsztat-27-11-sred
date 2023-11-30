import pandas as pd
import openpyxl

df = pd.DataFrame({'Osoba': ['Michał Jakub', 'Ewa Noga', 'Krzysztof Zawierucha'],
                   'Wynik': [15, 38, 21]})


def sprawdz(punkty):
    if punkty > 20:
        return "Zdany"
    else:
        return 'Oblany'


df.Wynik = df.Wynik.apply(sprawdz)
print(df)
df.to_excel("Egzamin.xlsx")
