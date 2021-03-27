import requests
response = requests.get("https://data.nasa.gov/resource/gvk9-iz74.json")

print(response.json())
