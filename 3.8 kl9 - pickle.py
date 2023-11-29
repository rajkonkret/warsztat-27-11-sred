import pickle

# biblioteka do łątwiejszego zapisywania obiektów do pliku

lista = [1, 2, 3, 4, 5]
print(type(lista))

# contex menager
# usprawnia działąnie np.:  z plikami, dba o obsługę błędów
with open('lista.txt', "w") as fh:
    fh.write(str(lista))

with open('lista.txt', "r") as file:
    data = file.read()

print(data)  # [1, 2, 3, 4, 5]
print(type(data))  # <class 'str'>
print(data[0])  # [

with open("lista.pickle", "wb") as file:
    pickle.dump(lista, file)

with open("lista.pickle", "rb") as f:
    p = pickle.load(f)

print(p)
print(type(p))  # <class 'list'>
print(p[0])  # 1

print(pickle.dumps(lista))
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
print(pickle.loads(b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'))
# [1, 2, 3, 4, 5]
