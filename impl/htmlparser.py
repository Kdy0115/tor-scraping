from bs4 import BeautifulSoup

class HtmlParser():
    def __init__(self, max_recall_num) -> None:
        self.max_recall_num = max_recall_num
        
    def parse(self, soup:BeautifulSoup) -> BeautifulSoup:
        elements = soup.find_all("meta")
        return elements