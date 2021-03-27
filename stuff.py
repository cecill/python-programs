import requests

data = requests.get('https://www.munster.us/About/Administration-and-Staff')

soup = BeautifulSoup(data.text, 'html.parser')