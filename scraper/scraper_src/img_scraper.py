from asyncio import Lock

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import Response
from rest_framework.status import HTTP_200_OK

from scraper_src.abstract_scraper import AbstractScraper


class ImageScraper(AbstractScraper):

    def __init__(self, locker: Lock):
        super().__init__(locker)

    def run_scraping(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        images = soup.find_all('img')
        images_db = ImageScraper.prepare_linked_images(images)
        ImageScraper.save_images_in_db(images_db)

    @staticmethod
    def prepare_linked_images(images) -> list:

        def check_source(link: str, prefix='') -> tuple:
            link = f'{prefix}{link}'
            response: Response = requests.get(link)
            content_type: str = response.headers.get('Content-Type')
            if response.status_code == HTTP_200_OK and 'image' in content_type:
                return True, link
            return False, link

        images_list = []
        for image in images:
            image: Tag
            alt = image.get('alt')
            src = image.get('src')
            correct_source = False
            if src and src.startswith('//'):
                correct_source, src = check_source(src, 'https:')
                if not correct_source:
                    correct_source, src = check_source(src, 'http:')
            elif src.startswith('http'):
                correct_source, src = check_source(src)
            else:
                correct_source, src = check_source(src, 'https://')
                if not correct_source:
                    correct_source, src = check_source(src, 'http://')
            if correct_source:
                # TODO create database entity and append to list
                images_list.append(image)
        return images_list

    @staticmethod
    def save_images_in_db(images):
        pass
