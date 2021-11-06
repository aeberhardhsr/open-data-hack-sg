import requests

def geo_code_swisstopo(addressString=None):
    params = { 'type': 'locations',
                'searchText': addressString,
                'sr': 2056,
                'limit': 1 }

    res = requests.get("https://api3.geo.admin.ch/rest/services/ech/SearchServer?", params=params)
    if res.status_code == 200:
        result = res.json()
        if "results" in result.keys() and len(result["results"]) > 0:
            likely_match = result["results"][0]["attrs"]
            return {
                    'latitude_lv95': int(likely_match['x']), 
                    'longitude_lv95' : int(likely_match['y']),
                    'egid' : likely_match["featureId"]}
        else:
            print(f'swisstopo no result while geocoding for '{addressString}'')
            return {}