# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(A, B):
    """
    Klasa dziedziczy po klasach A i B
    """

    def method(self):
        print("Metoda z klasy C")
        super().method()  # super() klasa/metoda nadrzędna C(A, B) w naszym przypadku A
        B.method(self)


class D(B, A):
    """
    Klasa D
    """

    def method(self):
        super().method()  # Metoda z klasy B


c = C()
c.method()  # Metoda z klasy A, ponadpisaniu Metoda z klasy C
# Metoda z klasy C
# Metoda z klasy A
# Metoda z klasy B
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

d = D()
d.method()  # Metoda z klasy B
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
