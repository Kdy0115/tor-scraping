import sys
sys.path.append('../')

from interface import ScrapingLogic
from impl.proxycontroller import TorProxyController
from impl.request import BeautifulRequest
from impl.htmlparser import HtmlParser

class ScrapingLogic(ScrapingLogic):
    def __init__(self, system_settings:dict) -> None:
        self.beautiful_request = BeautifulRequest(
            int(system_settings['REQUEST_WAIT_SECONDS_LEFT_LIMIT']),
            int(system_settings['REQUEST_WAIT_SECONDS_RIGHT_LIMIT']),
            int(system_settings['MAX_RECALL_NUM']))
                
        self.tor_proxy_controller = TorProxyController(
            system_settings['IP_CONFIRM_URL'],
            int(system_settings['TOR_PROXY_SERVER_PORT']),
            int(system_settings['TOR_PROXY_SERVER_RESTART_WAIT_SECONDS']),
            int(system_settings['MAX_RECALL_NUM']),
            system_settings['PROXY_TOR_CONTAINER_NAME'],
            self.beautiful_request)
        
        self.html_praser = HtmlParser(int(system_settings['MAX_RECALL_NUM']))
        
    def scraping(self, url: str) -> None:
        self.tor_proxy_controller.confirm_ip_address()
        for i in range(5):
            soup = self.beautiful_request.request(url)
            result = self.html_praser.parse(soup)
            print(result)
            self.tor_proxy_controller.restart_proxy()
            self.tor_proxy_controller.confirm_ip_address()
        