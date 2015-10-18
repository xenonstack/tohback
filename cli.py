#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" cli.py: tohback """

import sys
from  ConfigParser import ConfigParser
from scrapy.crawler import CrawlerProcess
import sources

__author__ = "Abhay Arora ( @BeliefLimitless )"
__copyright__ = "Copyright (c) 2015 Abhay Arora."
__email__ = "belieflimitless@icloud.com"
__date__ = "18/10/15"

def print_usage_information():
    print '''

---------------------------------------------
TOHBack - Web crawler for thoughtsonhealth.in
---------------------------------------------


Usage: tohback <command> [options]


Available commands:

        list-sources        List available source website.
        run-crawler         Runs web cralwer.

'''

if len(sys.argv) < 3:
    print_usage_information()
else:
    command = sys.argv[2]
    conf = ConfigParser()
    conf.read(sys.argv[1])
    if command == 'run-crawler':
        crawler = CrawlerProcess()
        crawler_name = str(conf.get('crawler', 'name'))
        keywords = []
        search_domain = []
        kw_str = conf.get('crawler', 'keywords')
        kws = kw_str.split(',')
        for kw in kws:
            fkw = kw.strip(' ').strip(',')
            keywords.append(fkw)
            search_domain.append(fkw)
        sd_str = conf.get('crawler', 'search_domain')
        sds = sd_str.split(',')
        for sd in sds:
            search_domain.append(sd.strip(' ').strip(','))
        for source in sources.__all__:
            crawler.crawl(source, name=crawler_name, keywords=keywords, search_domain = search_domain)
        crawler.start()
    elif command == 'list-sources':
        print '''
Available sources:
------------------'''
        for source in sources.__all__:
            print str(source)
        print ''
    else:
        print_usage_information()
