from pprint import pprint


class LongestKeyDict(dict):
    def longest_key(self):
        # zwraca najdłuzszy klucz w słowniku
        longest = None
        for key in self:  # iterujemy po kluczach
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


d1 = {'name': 'Radek', "test": "zdany"}
for k in d1:
    print(k)
# name
# test
for k, v in d1.items():
    print(k, "=>", v)
# name => Radek
# test => zdany

art = LongestKeyDict()
print(art)

art['tomasz'] = 12
art['abraham'] = 7
art['siedema'] = 9
art['radek'] = 3
art['zen'] = 1
print(art)
print(art.longest_key())  # abraham
pprint(art)
# {'tomasz': 12, 'abraham': 7, 'radek': 3, 'zen': 1}
# abraham
# {'abraham': 7, 'radek': 3, 'tomasz': 12, 'zen': 1}
