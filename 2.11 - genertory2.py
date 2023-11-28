generator_1 = [x for x in range(5)]
print(generator_1)  # [0, 1, 2, 3, 4]
print(type(generator_1))  # <class 'list'>

generator_2 = (x for x in [1, 2, 3, 4, 5])
print(type(generator_2))  # <class 'generator'>
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


def gen_4():
    i = 1
    while True:  # pętla nieskończona
        yield i * i
        i += 1


g4 = gen_4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fi = fibo()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fibo2 = fibo_with_index(10)
print(next(fibo2))  # (0, 0)
print(next(fibo2))  # (0, 0)
print(next(fibo2))  # (0, 0)
print(next(fibo2))  # (0, 0)
print(next(fibo2))  # (0, 0)

for i in fibo_with_index(10):
    print(f"Element {i}")  # Element (8, 21)

for i, n in fibo_with_index(10):
    print(f"pozycja {i}, element {n}")  # pozycja 9, element 34


def counter(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(c.send('OK'))
# OK
# 13
try:
    print(c.send("q"))  # StopIteration
except StopIteration:
    print("Generator zakończył działanie")  # Generator zakończył działanie
