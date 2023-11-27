try:
    # print("12" + 34)  # TypeError: can only concatenate str (not "int") to str
    # print(5 / 0)
    # print("A" + 5)
    # raise ValueError("Błąd wartości")
    # raise NameError("Bład nazwy")
    print(6 + 8)
except ValueError:
    print("Bład wartości")
except ZeroDivisionError:
    print("Nie dziel przez zero")  # Nie dziel przez zero
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład", e)
else:
    print("Tylko gdy bład nie wystąpil")
finally:
    print("Wykona się zawsze, niezależnie czy błąd sie pojawił, czy nie")

print("Program nadal działa")
