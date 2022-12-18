import requests

ips = set()

URL = "https://stat.ripe.net/data/country-resource-list/data.json"

PARAMS = {'resource': "IR", "v4_format": "prefix"}
r = requests.get(url=URL, params=PARAMS)
data = r.json()

file_json=open("ripe.json","w")
file_json.write(r.text)
file_json.close()

ipv4_list = data["data"]["resources"]["ipv4"]
ipv6_list = data["data"]["resources"]["ipv6"]

for d in ipv4_list:
    ips.add(d + "\n")
    print(d)

for d in ipv6_list:
    ips.add(d+ "\n")
    print(d)

file_output = open('ripe.txt', 'w')
file_output.writelines(sorted(ips))
file_output.close()