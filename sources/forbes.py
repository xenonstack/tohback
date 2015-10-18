#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" forbes.py: tohback """

from scrapy import Spider, Request
from bs4 import BeautifulSoup

__author__ = "Abhay Arora ( @BeliefLimitless )"
__copyright__ = "Copyright (c) 2015 Abhay Arora."
__email__ = "belieflimitless@icloud.com"
__date__ = "18/10/15"

class Forbes(Spider):

    start_urls = ['http://www.forbes.com']
    keywords = []

    def __init__(self, name, keywords = []):
        self.name = name
        self.keywords = keywords

    def parse(self, response):
        html = BeautifulSoup(response.body, 'html.parser')
        links = html.find_all('a')
        for word in self.keywords:
            if word in html.title.text:
                document = dict(
                    title = html.title.text
                )
                yield document
            for link in links:
                if word in str(link.text) or word in str(link.get('href')):
                    yield Request(link.get('href'), callback=self.parse)
