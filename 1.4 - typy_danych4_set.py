# set - przechowuje unikalne wartosci
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 77, 33, 11, 55, 33, 11]
zbior = set(lista)  # set() - zamiana na set, zbior
print(zbior)  # {33, 66, 11, 44, 77, 55}
zbior.add(18)
zbior.add(18)
zbior.add(33)
print(zbior)  # {33, 66, 11, 44, 77, 18, 55}
print(sorted(zbior))  # [11, 18, 33, 44, 55, 66, 77] zwróci liste

print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
# 33
# 66
# 11
# 44
# nie przyjmuje numeru indeksu
# print(zbior.pop(1))  # TypeError: set.pop() takes no arguments (1 given)
print(zbior)  # {77, 18, 55}

# usuniecie po elemencie
zbior.remove(18)
print(zbior)  # {77, 55}

zbior_liczb = {66, 11, 44, 18, 55, 62, 999, 999}
print(zbior_liczb)  # {66, 18, 55, 999, 11, 44, 62}

zb2 = set()  # deklaracja pustego seta
print(zb2)  # set() - wyswietlanie pustego zbioru

print(zbior | zbior_liczb)  # suma zbiorów {66, 999, 11, 44, 77, 18, 55, 62}
print(zbior & zbior_liczb)  # częśc wspolna {55}
print(zbior - zbior_liczb)  # różnica {77}
print(zbior.difference(zbior_liczb))  # {77}
# union() - nie mofyfikuje bazowych zbiorów
print(zbior.union(zbior_liczb))  # suma zbiorów, {66, 999, 11, 44, 77, 18, 55, 62}
print(zbior)  # {77, 55}
# update() - modyfikuje bazowy zbiór
zbior.update(zbior_liczb)
print(zbior)  # {66, 999, 11, 77, 44, 18, 55, 62}
# 14:45
