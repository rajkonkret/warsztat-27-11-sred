# napisanie funkcji, która za pomoca przekazanych argumentów
# zbuduje słownik i zwroci go
# first, name, age=None

def build_dict(first, name, age=None):
    person = {'first': first, 'name': name}
    if age:
        person['age'] = age

    return person


print(build_dict("radek", "Kowalski"))  # {'first': 'radek', 'name': 'Kowalski'}

while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by zakończyc")
    f_name = input("Imię:")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break
    age = input("Wiek: ")
    if age == "q":
        break

    print(build_dict(f_name, l_name, age))
# 13:25
