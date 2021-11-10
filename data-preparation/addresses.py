import json
<<<<<<< HEAD
from os import write
from geocode import geo_code_swisstopo
import requests
import csv
=======
import requests
>>>>>>> f841d12e8bfc9f40d3e1f3ea74ae3762e2be7248

addresses = []
coordinates_x = []
coordinates_y = []

with open('./new.json', 'r') as file:
    data = json.load(file)

for thing in data:
    addresses.append(thing['mainAddress']['street'])

#print(addresses)

#with open('addresses.txt', 'w') as f:
 #   for item in addresses:
  #      f.write("%s\n" % item)



#save the x,y coordinates
<<<<<<< HEAD
for item in addresses:
    #geo_code_swisstopo(item)
    #coordinates.append(item)
    params = { 'type': 'locations',
                'searchText': item,
                'sr': 4326,
                'limit': 1 }

    res = requests.get("https://api3.geo.admin.ch/rest/services/ech/SearchServer?", params=params)
    if res.status_code == 200:
        result = res.json()
        if "results" in result.keys() and len(result["results"]) > 0:
            for coordinate in result['results']:
                coordinates_x.append(coordinate['attrs']['x'])
                coordinates_y.append(coordinate['attrs']['y'])
                #f.write('{}, {}\n'.format(coordinate['attrs']['x'], coordinate['attrs']['y']))
                #print(coordinate['attrs']['x'], coordinate['attrs']['y'])
                    
        else:
            print(f'swisstopo no result while geocoding for {item}')


zip(coordinates_x, coordinates_y)
with open('coordinates.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(coordinates_x, coordinates_y))
=======
with open('coordinates.csv', 'w') as csvFile:
    for item in addresses:
        params = { 'type': 'locations',
                    'searchText': item,
                    'sr': 4326,
                    'limit': 1 }
>>>>>>> f841d12e8bfc9f40d3e1f3ea74ae3762e2be7248

        res = requests.get("https://api3.geo.admin.ch/rest/services/ech/SearchServer?", params=params)
        if res.status_code == 200:
            result = res.json()
            if "results" in result.keys() and len(result["results"]) > 0:
                likely_match = result["results"][0]["attrs"]
                csvFile.write('{}, {}\n'.format((likely_match['x']),(likely_match['y'])))
            else:
                print(f'swisstopo no result while geocoding for {item}')
    