from multiprocessing import Lock
from bs4 import BeautifulSoup

from scraper_src.abstract_scraper import AbstractScraper


class TextScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        visible_text: str = soup.getText()
        TextScraper.prepare_text_lines(visible_text)

    @staticmethod
    def prepare_text_lines(visible_text) -> list:
        text_list = []
        lines = visible_text.split('\n')
        for line in lines:
            if not line or len(line) - 1 <= line.count(' '):
                continue
            # TODO create db entity with text and append to list
            text_list.append(line)
        return text_list
