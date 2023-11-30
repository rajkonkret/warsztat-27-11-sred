from pydantic import BaseModel
import requests as re

url = 'https://randomuser.me/api/'
response = re.get(url)
data = response.json()
print(data)
user = data['results'][0]
print(user)
print(f"Imię: {user['name']['first']}, nazwisko: {user['name']['last']}")
print(f"Email: {user['email']}")
photo_url = user['picture']['large']  # https://randomuser.me/api/portraits/women/92.jpg
response_photo = re.get(photo_url)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)

print("Zdjęcie zapisane")


# "name": {
#         "title": "Monsieur",
#         "first": "Simon",
#         "last": "Roger"
#       },

class Name(BaseModel):
    title: str
    first: str
    last: str


# "picture": {
#         "large": "https://randomuser.me/api/portraits/men/53.jpg",
#         "medium": "https://randomuser.me/api/portraits/med/men/53.jpg",
#         "thumbnail": "https://randomuser.me/api/portraits/thumb/men/53.jpg"
#       },
class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    name: Name
    email: str
    picture: Picture


user_info = UserInfo(**user)
print(user_info)

photo_url = user_info.picture.large
response_photo_pydantic = re.get(photo_url)
with open('user_photo_pydantic.jpg', 'wb') as f:
    f.write(response_photo_pydantic.content)
