import requests
from bs4 import BeautifulSoup

query = 'Lista de países por PIB nominal'

url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")
html = requests.get(url)
data = html.json()
print(html) 