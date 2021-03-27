import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://data.nasa.gov/resource/gvk9-iz74.json")
print(response.status_code)
print(response.json())

jprint(response.json())