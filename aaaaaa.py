import requests
from bs4 import BeautifulSoup

url = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
res = requests.get(url)
html = BeautifulSoup(res.text, 'lxml')

for tag in html.find_all('img'):
    url = tag.get('alt')
    print(url)