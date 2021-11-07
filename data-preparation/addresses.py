import json
import requests

addresses = []
coordinates = []

with open('./new.json', 'r') as file:
    data = json.load(file)

for thing in data:
    addresses.append(thing['mainAddress']['street'])

#print(addresses)

#with open('addresses.txt', 'w') as f:
 #   for item in addresses:
  #      f.write("%s\n" % item)

#save the x,y coordinates
with open('coordinates.csv', 'w') as csvFile:
    for item in addresses:
        params = { 'type': 'locations',
                    'searchText': item,
                    'sr': 4326,
                    'limit': 1 }

        res = requests.get("https://api3.geo.admin.ch/rest/services/ech/SearchServer?", params=params)
        if res.status_code == 200:
            result = res.json()
            if "results" in result.keys() and len(result["results"]) > 0:
                likely_match = result["results"][0]["attrs"]
                csvFile.write('{}, {}\n'.format((likely_match['x']),(likely_match['y'])))
            else:
                print(f'swisstopo no result while geocoding for {item}')
    