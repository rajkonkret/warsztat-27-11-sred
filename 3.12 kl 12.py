# hermetezycja, enkapsulacja
class Boat:
    """
    Dokumantacja klasy
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # pole prywatne

    def sail(self):
        self.__speed += 20
        self.__private()

    def speedometer(self):
        print(f"Speed in knots {self.__speed}")

    def break_(self):  # użycie zkazanej nazwy braka w konwencji nazewniczej pythonna
        self.__speed -= 20

    def __private(self):  # metoda prywatna
        print("Private")


b1 = Boat("Omega", 2023)
b1.sail()
b1.sail()
b1.sail()
b1.sail()
# print(b1.__speed)  # 80, po ustawieniu jako prywatne __speed-> AttributeError: 'Boat' object has no attribute '__speed'
b1.speedometer()  # Speed in knots 80
b1.break_()
b1.break_()
b1.break_()
b1.speedometer()
b1.__speed = 0  # pole globalne klasy przypadkowo o tej samej nazwie co nasze pole prywatne
print(b1.__speed)
b1.speedometer()
