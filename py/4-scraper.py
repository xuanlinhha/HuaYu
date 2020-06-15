# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import time
from bs4 import BeautifulSoup

def get_char_info(char):
    url = 'https://hvdic.thivien.net/whv/' + char
    resp = requests.get(url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    # OK
    with open('../output/char_data/'+char+'.html', 'w') as out_file:
        out_file.write(resp.text)

def crawl(path):
    counter = 0
    with open(path) as fp:
        for line in fp:
            get_char_info(line.strip())
            print('finished ' + line.strip() + ' !')
            time.sleep(1)
            counter = counter + 1
            if counter == 600:
                time.sleep(600)

crawl('../tmp.txt')
