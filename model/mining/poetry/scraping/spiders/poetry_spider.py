import scrapy
from bs4 import BeautifulSoup
from scraping.items import Poem
from typing import List

class PoetrySpider(scrapy.Spider):
    name = 'poetry'

    start_urls = [f"https://www.ukrlib.com.ua/books/printit.php?tid={id}" for id in range(100000)]
        
    def parse(self, response):
        name = self.extract_poetry_name(response)
        author = self.extract_author_name(response)
        content = self.extract_poetry_content(response)
        if content:
            yield Poem(name=name, written_by=author, poem=content)

    def extract_poetry_name(self, response):
        return response.css("div.page-title > h1::text").get()
    
    def extract_author_name(self, response):
        return response.css("div.page-title > h2::text").get()
    
    def extract_poetry_content(self, response):
        soup = BeautifulSoup(response.css("#content").get(), 'html.parser')
        for s in soup.select('div'):
            s.extract()
        return self.clean_poem(soup.find_all(text=True))

    def clean_poem(self, poem: List[str]) -> str:
        cleaned = []
        for line in poem:
            remove_newline = line.replace("\n", "")
            remove_trailing_spaces = str.strip(remove_newline)
            if remove_trailing_spaces  \
               and not remove_trailing_spaces.startswith(".") \
               and not remove_trailing_spaces.startswith("/"):
                cleaned.append(remove_trailing_spaces)

        if all(len(x) < 50 for x in cleaned) and len(cleaned) < 50:
            return str.join("\n", cleaned)
        return ""

