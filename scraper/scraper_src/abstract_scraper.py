from abc import ABC, abstractmethod
from multiprocessing import Lock


class AbstractScraper(ABC):

    def __init__(self, locker: Lock):
        self._locker = locker

    @property
    def locker(self):
        return self._locker

    @abstractmethod
    def run_scraping(self, content, web_entity):
        pass
