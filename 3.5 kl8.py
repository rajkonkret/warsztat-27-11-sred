from abc import ABC, abstractmethod


# po oznaczeniu metody jako abstrakcyjnej klasa staje sie abstarakcyjna
# oznacza to, że nie mozemy stworzyc obiektu tej klasy, mozmy tylko klas dziedziczących
# obowiązkowo w klasach dziedziczących musimy nadpisc metody abstrakcyjne
# TypeError: Can't instantiate abstract class Counter with abstract method drukuj
class Counter(ABC):

    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # metoda abstrakcyjna
    def drukuj(self):
        pass

    @staticmethod
    def from_string():
        return "Format string %d"

    @classmethod
    def from_counter(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość nie może byc większa niż MAX")
        super().__init__(values)

    # obowiązkowo musze nadpisac metodę drukuj bo jest abstrakcyjna
    def drukuj(self):
        print(f"Drukuje...", self.values)


# klasa/metoda abstrakcyjna - nie moge stworzyc obiektu tej klasy

bc = BoundedCounter()
bc.increment()
bc.drukuj()

# metoda statyczna
# wywołujemy bez tworzenia obiektu klasy
print(Counter.from_string())  # Format string %d
# niezależna od obiektu
bc.from_string()
# classmethod
# metoda tworzy obiekt klasy na podstawie innego obiektu tej klasy
d = BoundedCounter.from_counter(bc)
d.drukuj()  # Drukuje... 1
e = BoundedCounter(bc.values)
e.drukuj()  # Drukuje... 1
# 11:30
