# match case
lang = input("Podaj znany Ci język programowania")
# input zwraca str

match lang.lower().replace(" ", ""):
    case "java":
        print("Lubię jave")
    case "python":
        print("Miał być prosty")
    case "c++":
        print("Kto to jeszce używa?")
    case _:
        print("Działanie domyślne")
