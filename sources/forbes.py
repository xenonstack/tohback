#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" forbes.py: tohback """

from scrapy import Spider, Request
from bs4 import BeautifulSoup
import urlparse
import re
import json
import time

__author__ = "Abhay Arora ( @BeliefLimitless )"
__copyright__ = "Copyright (c) 2015 Abhay Arora."
__email__ = "belieflimitless@icloud.com"
__date__ = "18/10/15"

class Forbes(Spider):

    allowed_domains = ["forbes.com", "forbesconferences.com"]
    start_urls = ['http://www.forbes.com']
    keywords = []

    def __init__(self, name, keywords = [], search_domain = []):
        self.name = name
        self.keywords = keywords
        self.search_domain = search_domain

    def parse(self, response):
        html = BeautifulSoup(response.body, 'html.parser')
        links = html.find_all('a')
        scripts = html.find_all('script')
        regex = re.compile('(fbs_settings.content)( *)(=)(.*)(;)')
        for word in self.keywords:
            if word in html.title.text.lower():
                for script in scripts:
                    parsed = regex.findall(script.text)
                    if len(parsed) > 0:
                        dataobj = json.loads(parsed[0][3])
                        if 'content' in dataobj.get('id'):
                            document = dict(
                                source = 'forbes',
                                uid = dataobj.get('id'),
                                crawl_time = time.time(),
                                data = parsed[0][3]
                            )
                            yield document
        for word in self.search_domain:
            for link in links:
                if link.get('href') != None and word in link.get('href'):
                    next_link = link.get('href')
                    if not urlparse.urlparse(next_link).scheme:
                        next_link = response.urljoin(next_link)
                    yield Request(next_link, callback=self.parse)

