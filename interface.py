import abc
from bs4 import BeautifulSoup
import urllib.request

class ScrapingLogic(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def scraping(self, url:str) -> None:
        raise NotImplementedError()
    
class Request(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _create_request(self, url:str) -> urllib.request.Request:
        raise NotImplementedError    
    @abc.abstractmethod
    def request(self, url:str) -> BeautifulSoup:
        raise NotImplementedError
    
class proxyController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def confirm_ip_address(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def restart_proxy(self) -> None:
        raise NotImplementedError()