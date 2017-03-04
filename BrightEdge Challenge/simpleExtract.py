#!/usr/local/bin/python
# -- coding: utf-8 --
import json, urllib
import re

def collect_data(url):
    #Function to collect data from given Url
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data