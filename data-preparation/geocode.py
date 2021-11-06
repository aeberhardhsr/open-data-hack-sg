import requests

def geo_code_swisstopo(addressString=None):
    params = { 'type': 'locations',
                'searchText': addressString,
                'sr': 4376,
                'limit': 1 }

    res = requests.get("https://api3.geo.admin.ch/rest/services/ech/SearchServer?", params=params)
    if res.status_code == 200:
        result = res.json()
        if "results" in result.keys() and len(result["results"]) > 0:
            likely_match = result["results"][0]["attrs"]
            with open ('coordinates.py', 'w') as f:
                f.write("%s\n" % 'latitude_lv95: {}'.format(int(likely_match['x'])), 'longitude_lv95: {}'.format(int(likely_match['y'])))
        else:
            print(f'swisstopo no result while geocoding for {addressString}')
            return {}