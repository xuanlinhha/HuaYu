# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import requests
import time
from bs4 import BeautifulSoup

def has_data(name, folder):
    path = os.path.join(folder, name + '.html')
    if not os.path.exists(path):
        return False
    df = open(path)
    content = df.read()
    df.close()
    if 'html' not in content:
        return False
    return True

def request_char_data(char, out_folder):
    path = os.path.join(out_folder, char + '.html')
    
    url = 'https://hvdic.thivien.net/whv/' + char
    resp = requests.get(url)
    if resp.status_code != 200:
        print('ERROR with {}, Status = {}'.format(char, resp.status_code))
    with open(path, 'w') as out_file:
        out_file.write(resp.text)

def scrap(chars_src, out_folder):
    with open(chars_src) as fp:
        for line in fp:
            if not has_data(line.strip(), out_folder):
                request_char_data(line.strip(), out_folder)
                print('finished ' + line.strip() + ' !')
            else:
                print('existed ' + line.strip() + ' !')

scrap('../output1/characters.txt', '../hvdict/char_data')
