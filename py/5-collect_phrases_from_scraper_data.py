# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import time
import json
import os
from ordered_set import OrderedSet
from bs4 import BeautifulSoup

def collect_phrases(html):
    phrases = {}
    soup = BeautifulSoup(html, features="html.parser")
    ws_tag = soup.find(string=re.compile('Từ ghép .*'))
    if ws_tag:
        ws = ws_tag.find_parent('p').find_next('div').find_all('a')
        for w in ws:
            text = w.string
            lastsp = text.rfind(' ')
            phrases[text[lastsp+1:]] = text[0:lastsp]
    return phrases

def collect_all_phrases(path):
    chars_no_data = OrderedSet()
    char_phrases = []
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        char = line.strip()
        # no data file
        if not os.path.exists('../output/char_data/'+char+'.html'):
            chars_no_data.add(char)
        else: 
            df = open('../output/char_data/'+char+'.html')
            content = df.read()
            df.close()
            if 'html' not in content:
                chars_no_data.add(char)
            else:
                phrases = collect_phrases(content)
                char_phrases.append(json.dumps({'char':char, 'phrases': phrases}, ensure_ascii=False))

    # write chars with pharases
    print('total chars with phrases: {}'.format(len(char_phrases)))
    fo = open('../output/ONLINE_CHAR_PHRASES.TXT', 'a')
    for cp in char_phrases:
        fo.write("%s\n" % cp)
    fo.close()

    # save remaining
    print('characters without data: '.format(len(chars_no_data)))
    for char in chars_no_data:
        print(char)

collect_all_phrases('../output/TRADITIONAL_CHARS.TXT')
