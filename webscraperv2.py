import scrapy


class NewsSpider(scrapy.Spider):
    name = "testiclegobbler"
    start_urls = ["https://news.google.com"]