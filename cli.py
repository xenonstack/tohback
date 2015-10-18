#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" cli.py: tohback """

import sys

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
    if command == 'run-crawler':
        pass
    else:
        print_usage_information()
