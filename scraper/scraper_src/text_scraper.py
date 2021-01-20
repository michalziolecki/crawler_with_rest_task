from multiprocessing import Lock
from bs4 import BeautifulSoup

from scraper_src.abstract_scraper import AbstractScraper


class TextScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        visible_text: str = soup.getText()
        lines = visible_text.split('\n')
        for line in lines:
            if not line or len(line) - 1 <= line.count(' '):
                continue
            print(f'{line}')
