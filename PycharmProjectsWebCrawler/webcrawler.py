import requests
from bs4 import BeautifulSoup


def get_movie_links(url):
    source_code = requests.get(url)
    plain_txt = source_code.text
    soup = BeautifulSoup(plain_txt, "html.parser")
    for link in soup.findAll('a', {'class': 'bbc_url'}):
        href = link.get('href')
        title = link.string
        print(title)
        print(href)


get_movie_links(r'http://tamilrockers.gs/')
