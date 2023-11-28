# funkcja rekurencyjna - funkcja wywołuja sama siebie

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


print(nwd(48, 18))  # 6
print(silnia(5))  # 120
