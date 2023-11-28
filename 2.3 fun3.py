def example(a, b, /, d=0, **kwargs):
    print("a, b", a, b)
    print("d", d)
    print(kwargs)
    print(f"e {kwargs.get('e', 'default')}")
    return a * b


def all_params(*args, **kwargs):  # * - pozycyjne, ** - nazwane
    pass


example(1, 2)
print(example.__code__.co_varnames)  # ('a', 'b', 'd', 'kwargs')
# example(b=9, a=7)  # TypeError: example() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argumenty ktore musza byc podane po pozycji od argumentów, które mogą byc podane po nazwie
print(example(1, 2, 3))  # d 3
print(example(1, 2, 3, e=9))  # {'e': 9} - argumenty słownikowe
print(example(1, 2, d=3, e=9))  # d 3
print(example(1, 2, d=3, e=9, a=9))  # {'e': 9, 'a': 9}
