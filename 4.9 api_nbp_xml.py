import requests
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = requests.get(url)
xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x0000019373AD80E0>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

data = root.find(".//EffectiveDate").text
print(f"Data tabeli: {data}")  # Data tabeli: 2023-11-30

no = root.find(".//No").text
print(f"Numer tabeli: {no}")  # Numer tabeli: 232/A/NBP/2023

rates = root.findall('.//Rate')
print(rates)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = float(rate.find('Mid').text)
# 15:10
