from bs4 import BeautifulSoup
import urllib.request

class Eto_sp:


    def __init__(self, url):
        self.url = url

    def scrape(self):
        r = urllib.request.urlopen(self.url)
        html = r.read()
        parser = 'html.parser'
        bs = BeautifulSoup(html, 'lxml')
        aaa = bs.find(id='rank').find_all('img')
        url = [i.attrs.get('alt', '') for i in aaa if '座' in i.attrs.get('alt', '')]
        print(url[::2])

news = 'https://fortune.yahoo.co.jp/12astro/ranking.html'
Eto_sp(news).scrape()

