import urllib.request
import json
contents = urllib.request.urlopen("https://api.nasa.gov/neo/rest/v1/neo/3802394?api_key=DEMO_KEY").read()
varab = json.loads(contents)
print(varab)