import sys
sys.path.append('..')
import subprocess
import time
import socket, socks
import ssl

from interface import proxyController
from impl.request import BeautifulRequest

class TorProxyController(proxyController):
    def __init__(
        self, 
        confirm_page_url:str, 
        port:int, 
        restart_wait_time_seconds:int, 
        max_recall_num:int, 
        proxy_container_name:str,
        request:BeautifulRequest) -> None:
        
        self.port = port
        self.restart_wait_time_seconds = restart_wait_time_seconds
        self.max_recall_num = max_recall_num
        self.confirm_url = confirm_page_url
        self.request = request
        self.proxy_container_name = proxy_container_name
        
    def confirm_ip_address(self) -> None:
        soup = self.request.request(self.confirm_url)
        current_ip_address = soup.body.text.split(': ')[1]
        print("Current IP address: {}".format(current_ip_address))
        
    def restart_proxy(self) -> None:
        print('Restart proxy server')
        subprocess.run(['docker restart {}'.format(self.proxy_container_name)], shell=True)
        time.sleep(self.restart_wait_time_seconds)
        ssl._create_default_https_context = ssl._create_unverified_context
        socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, 'proxy', self.port)
        socket.socket = socks.socksocket      
        