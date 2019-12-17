# -*- coding: utf-8 -*-
import scrapy


class FilmcrawlerSpider(scrapy.Spider):
    name = 'filmCrawler'
    start_urls = ['http://phimmoi.net/']

    def parse(self, response):
        pass
