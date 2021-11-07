import json
from geocode import geo_code_swisstopo

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
for item in addresses:
    geo_code_swisstopo(item)
    #coordinates.append(item)

