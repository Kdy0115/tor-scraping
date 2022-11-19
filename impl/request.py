import sys
sys.path.append('..')
from bs4 import BeautifulSoup
import urllib.request as urlreq
import random
import time

from interface import Request

class BeautifulRequest(Request):
    def __init__(
        self, 
        request_wait_seconds_left_limit:int, 
        request_wait_seconds_right_limit:int, 
        max_recall_num:int) -> None:
        
        self.max_call_num = max_recall_num
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        self.request_wait_seconds_left_limit = request_wait_seconds_left_limit
        self.request_wait_seconds_right_limit = request_wait_seconds_right_limit
        
    def _wait(self):
        random_time_seconds = random.uniform(self.request_wait_seconds_left_limit, self.request_wait_seconds_right_limit)
        time.sleep(random_time_seconds)
        
    def _create_request(self, url: str) -> urlreq.Request:
        req = urlreq.Request(url)
        req.add_header = self.header
        return req
        
    def request(self, url: str): 
        req = self._create_request(url)
        res = urlreq.urlopen(req)
        soup = BeautifulSoup(res, 'lxml')
        print("Request Success")
        return soup
        