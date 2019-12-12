import requests
from bs4 import BeautifulSoup

def scrapper(clase, distritos, num):
    limit = [e for e in range(1,num)]
    homes = []
    for distrito in distritos:
        for number in limit:
            url = 'https://www.fotocasa.es/es/alquiler/viviendas/madrid-capital/{}/l/{}'.format(distrito, number)
            soup = BeautifulSoup((requests.get(url)).text, 'html.parser')
            homes += soup.select(clase)
    html = [e.text for l in homes for e in l]
    output = [e for e in html if e != '' and e != 'PUBLICIDAD']
    return output