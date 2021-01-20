from multiprocessing import Lock
from bs4 import BeautifulSoup

from scraper_src.abstract_scraper import AbstractScraper


class TextScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content):
        print(f'type=={type(content)}')
        soup = BeautifulSoup(content, 'html.parser')
        # soup.find_all('img')
