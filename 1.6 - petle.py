# for - petla iteracyjna

for i in range(10):  # 0 .. 9
    print(i)

for i in range(10):
    for j in range(10):
        print(i, j)  # 9 9

lista2 = [j for j in range(6)]  # budowanie listy w jednej linijce
# list comprehesion
print(lista2)  # [0, 1, 2, 3, 4, 5]

for c in lista2:
    print(c)

# instrukcje warunkowe
# if
# if warunek:
#   operacja gdy warunek poprawny (True)
# else:
#   w przeciwnym przypadku

# a = 1
a = 2
if a == 1:
    print(f"A równa się 1")
else:
    print(f"A nie równa się 1")
# A równa się 1 dla a = 1
# A nie równa się 1 dla a = 2
a = 1
if a == 1:
    print(f"A równa się 1")
elif a == 2:
    print(f"A równa się 2")
elif a == 3:
    print(f"A równa się 3")
else:
    print(f"A nie równa się 1 ani 2 ani 3")

print("program nadal działa")
a = 20
if a > 0:
    print("A > 0")
elif 0 < a < 10:  # a > 0 and a < 10
    print("A > 0 i A < 01")
elif a > 10:
    print("A > 10")
# A > 0

for c in lista2:
    if c % 2 == 0:
        print(c, "parzysta")
    if c == 3:
        print(c)

lista4 = [j for j in range(6) if j % 2 == 0]
print(lista4)  # [0, 2, 4]
