from pydantic import BaseModel
from typing import List
import requests as re

# requests - biblioteka do korzystania z zapytan hhtp do pobierania dannych z internetu

url = 'http://api.open-notify.org/astros.json'
response = re.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx - błedy przekierowania
# 4xx - błedy uzytkownika np 404, 400 Bad Request
# 5xx - błedy po stronie serwera np.: 500
rj = response.json()
print(rj)
print(type(rj))
print(rj['people'])


class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]


data = AstroData(**response.json())
print(data)
# message='success' people=[Astronaut(name='Jasmin Moghbeli', craft='ISS'),
# Astronaut(name='Andreas Mogensen', craft='ISS'),
# Astronaut(name='Satoshi Furukawa', craft='ISS'),
# Astronaut(name='Konstantin Borisov', craft='ISS'),
# Astronaut(name='Oleg Kononenko', craft='ISS'),
# Astronaut(name='Nikolai Chub', craft='ISS'),
# Astronaut(name="Loral O'Hara", craft='ISS')]
print(data.message)
print(data.people)
for astronaut in data.people:
    print(f"{astronaut.name}, {astronaut.craft}")

# Jasmin Moghbeli, ISS
# Andreas Mogensen, ISS
# Satoshi Furukawa, ISS
# Konstantin Borisov, ISS
# Oleg Kononenko, ISS
# Nikolai Chub, ISS
# Loral O'Hara, ISS

# 13:30
