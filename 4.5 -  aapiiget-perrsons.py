import requests as re
from pydantic import BaseModel

url = 'https://restcountries.com/v3.1/name/Poland'

response = re.get(url)
data = response.json()
print(data)
country = data[0]
print(country['name'])
# {'common': 'Poland', 'official': 'Republic of Poland', 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
print(f"Nazwa kraju: {country['name']['common']}")  # Nazwa kraju Poland
print(f"Stolica kraju: {country['capital'][0]}")  # Stolica kraju: Warsaw
print(f"Liczba ludności: {country['population']}")


# {'common': 'Poland',
# 'official': 'Republic of Poland',
# 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}

class Name(BaseModel):
    common: str
    official: str
    nativeName: dict


class CountryInfo(BaseModel):
    name: Name
    capital: list[str]
    population: int


country_data = [CountryInfo(**data) for data in response.json()]
print(country_data)
# [CountryInfo(name={'common': 'Poland', 'official': 'Republic of Poland',
#                    'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}},
#              capital=['Warsaw'], population=37950802)]
print(type(country_data[0]))  # <class '__main__.CountryInfo'>
print(country_data[0].name)
# {'common': 'Poland',
# 'official': 'Republic of Poland',
# 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
