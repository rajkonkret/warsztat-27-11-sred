# __missing__ - metoda jest wykonywany gdy wywołujemy klucz, którego nie ma w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


# tak zmienic metody by w razie braku klucza dodawałą go z domyslna wartoscia
class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0


# dopuszczamy podczas uzycie nie dbania o duze/małe litery
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        # return self[key.lower()]
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}
d_python['name'] = 'Radek'
print(d_python)
print(d_python['name'])
# print(d_python['imie'])  # KeyError: 'imie'

d1 = DefaultDict()
d1['name'] = 'Radek'
print(d1['name'])
print(d1['imie'])  # default

d2 = AutoKeyDict()
print(d2)  # {}
print(d2['imie'])
print(d2)  # {'imie': 0}

d3 = CaseInsensitiveDict()
d3['name'] = "Radek"
print(d3['NamE'])  # Radek

d_python[(3,)] = 0
print(d_python)  # {'name': 'Radek', (3,): 0}
