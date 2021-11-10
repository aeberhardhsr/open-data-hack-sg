import requests
import json

def geo_code_swisstopo(addressString=None):
    params = { 'type': 'locations',
                'searchText': addressString,
                'sr': 4326,
                'limit': 1 }

    res = requests.get("https://api3.geo.admin.ch/rest/services/ech/SearchServer?", params=params)
    if res.status_code == 200:
        result = res.json()
        if "results" in result.keys() and len(result["results"]) > 0:
            for coordinate in result['results']:
                #with open('coordinates.csv', 'w') as f:
                print(coordinate['attrs']['x'], coordinate['attrs']['y'])
                    
        else:
            print(f'swisstopo no result while geocoding for {addressString}')
            return {}