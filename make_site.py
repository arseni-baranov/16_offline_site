import requests
from bs4 import BeautifulSoup

ROOT_URL = "http://getbootstrap.com/"
THEME_URL = "{}examples/jumbotron/".format(ROOT_URL)


def find_links(html_soup):
    print(html_soup.findAll('link', href=True))
    src_links = html_soup.findAll('script')


def main():
    html_doc = requests.get(THEME_URL).text
    print(html_doc)
    html_soup = BeautifulSoup(html_doc, 'lxml')
    find_links(html_soup)

if __name__ == "__main__":
    main()