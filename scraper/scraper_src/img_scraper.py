from asyncio import Lock

from bs4 import BeautifulSoup
from bs4.element import Tag
from scraper_src.abstract_scraper import AbstractScraper


class ImageScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        images = soup.find_all('img')
        print(f' images={images}')
        images_db = ImageScraper.prepare_linked_images(images)
        ImageScraper.save_images_in_db(images_db)

    @staticmethod
    def prepare_linked_images(images) -> list:
        images_list = []
        for image in images:
            image: Tag
            alt = image.get('alt')
            src = image.get('src')
            print(f'0source={src}')
            if src and src.startswith('//'):
                src = src[2:]
            # TODO create database entity and append to list
            images_list.append(image)
        return images_list

    @staticmethod
    def save_images_in_db(images):
        pass
