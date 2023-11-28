# dekoratora który zamienia tekst  na duze litery (funkcja przekaza zwraca jakis tekst)
def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper():
        result = func()
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!"


print(greeting())  # HELLO WORLD!
print("HELLO WORLD!")
# HELLO WORLD!
