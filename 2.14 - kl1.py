# klasa - szablon
# pola
# funkcje

import math


# math - do matematycznych zastosowan
# definicja klasy
class MyFirstClass:
    """
    Klasa w Pythonie, reprezentująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0) -> None:  # to są tylko podpowiedzi typów
        """
        metoda inicjalizujaca (tzw. konstruktor)
        :param x: x: int
        :param y: y: int
        """
        # self.x = x
        # self.y = y
        # dodalismy funkcje move która robi to samo
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    # funkcja magiczna odpowiadająca za np,: sposób w jaki obiekt zostanie wypisany na ekranie
    def __repr__(self):
        return f"x= {self.x}, y= {self.y}"


p1 = MyFirstClass()  # stworzenie obietku klasy
# Wielolinijkowy komentarz jest traktowany jako dokumentacja dla klasy czy funkcji
print(MyFirstClass.__doc__)  # Klasa w Pythonie, reprezentująca punkty w przestrzeni x i y
print(print.__doc__)
print(p1.x)
print(p1.y)
p1.move(100, 69)
print(p1)  # <__main__.MyFirstClass object at 0x0000023E3344C250>
# po nadpisaniu __repr__
# x= 100, y = 69
p1.reset()
print(p1)  # x= 0, y= 0
p2 = MyFirstClass(100, 54)
print(p2)  # x= 100, y= 54
print(p1.calculate(p2))  # 113.64858116140297
print(p1.__str__())  # x= 0, y= 0
