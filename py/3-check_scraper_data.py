# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import os
from bs4 import BeautifulSoup
from ordered_set import OrderedSet

def check(path):
    chars_without_data = OrderedSet()
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        char = line.strip()
        # no data file
        if not os.path.exists('../output/char_data/'+char+'.html'):
            chars_without_data.add(char)
        else:
            df = open('../output/char_data/'+char+'.html')
            content = df.read()
            df.close()
            # empty content
            if 'html' not in content:
                chars_without_data.add(char)

    # write char set with no data
    for char in chars_without_data:
        print(char)
    print('chars_without_data = {}'.format(len(chars_without_data)))

check('../output/TRADITIONAL_CHARS.TXT')
