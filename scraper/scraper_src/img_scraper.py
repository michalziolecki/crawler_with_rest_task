from asyncio import Lock

from bs4 import BeautifulSoup

from scraper_src.abstract_scraper import AbstractScraper


class ImageScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        images = soup.find_all('img')
        print(f'images={images}')