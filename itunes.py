import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=4))
#what json.dumps necessarily does is that it prints json texts in a prettier way

o = response.json()
for result in o["results"]:
    print(result["trackName"])