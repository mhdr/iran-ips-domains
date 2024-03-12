import requests

url = "https://stat.ripe.net/data/country-resource-list/data.json"

params = {'resource': "IR", "v4_format": "prefix"}
response = requests.get(url, params=params)
print(response.text)