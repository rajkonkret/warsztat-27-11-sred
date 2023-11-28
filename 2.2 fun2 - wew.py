# funkcja wewnętrzna  (zagnieżdzona)
# dekorator wykorzystuje zasady działąnia funkcji wewnętrznej

def fun1():
    print("To jest funkcja fun1")

    def fwew(a, b):
        return a * b

    return fwew  # chcemy zwrocic tylko adres funkcji (referencje)


print(fun1())  # <function fun1.<locals>.fwew at 0x000001D1C18B8E00>
x = fun1()
print(x)  # <function fun1.<locals>.fwew at 0x0000018FFBCA8E00>
print(type(x))  # <class 'function'>
# x()  # TypeError: fun1.<locals>.fwew() missing 2 required positional arguments: 'a' and 'b'
print((x(7, 8)))  # 56
