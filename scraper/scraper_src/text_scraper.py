from multiprocessing import Lock
from bs4 import BeautifulSoup

from scraper_src.abstract_scraper import AbstractScraper
from data.utils import include_django_orm

include_django_orm()

from data.models import TextData


class TextScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content, web_entity):
        with self.locker:
            soup = BeautifulSoup(content, 'html.parser')
            visible_text: str = soup.getText()
            TextScraper.prepare_text_and_save_in_db(visible_text, web_entity)

    @staticmethod
    def prepare_text_and_save_in_db(visible_text, web_entity):
        lines = visible_text.split('\n')
        for line in lines:
            if not line or len(line) - 1 <= line.count(' '):
                continue
            text_entity = TextData(related_web_addr=web_entity, text=line)
            text_entity.save()
