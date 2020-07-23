# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import time
import json
import os
import pickle
from ordered_set import OrderedSet
from collections import OrderedDict
from bs4 import BeautifulSoup

def get_data(path):
    res = OrderedSet()
    f = open(path)
    for line in f:
        if ' ' in line:
            res.add(line.split()[1].strip().replace('，', '').replace('.', ''))
        else:
            res.add(line.strip().replace('，', '').replace('.', ''))
    f.close
    return res

def get_char_meaning(chars_src, data_folder):
    res = []
    count = 0
    chars = get_data(chars_src)
    for char in chars:
        data_file = os.path.join(data_folder, char + '.html')
        if not os.path.exists(data_file):
            print('{} has no data!'.format(char))
            continue
        else:
            soup = BeautifulSoup(open(data_file), features="html.parser")

        meaning = OrderedDict()
        meaning['char'] = char

        # pho thong
        pho_thong = soup.find(string=re.compile('Từ điển phổ thông'))
        contents = []
        if pho_thong:
            contents = filter(lambda e: e.name != 'br', pho_thong.parent.find_next_sibling('div').contents)
            contents = list(map(lambda e: e.strip(), contents))
            meaning['pho_thong'] = contents

        # trich_dan
        trich_dan = soup.find(string=re.compile('Từ điển trích dẫn'))
        contents = []
        if trich_dan:
            contents = filter(lambda e: e.name != 'br', trich_dan.parent.find_next_sibling('div').contents)
            contents = list(map(lambda e: e.strip(), contents))
            meaning['trich_dan'] = contents

        # thieu_chuu
        thieu_chuu = soup.find(string=re.compile('Từ điển Thiều Chửu'))
        contents = []
        if thieu_chuu:
            contents = filter(lambda e: e.name != 'br', thieu_chuu.parent.find_next_sibling('div').contents)
            contents = list(map(lambda e: e.strip(), contents))
            meaning['thieu_chuu'] = contents

        # tran_van_chanh
        tran_van_chanh = soup.find(string=re.compile('Từ điển Trần Văn Chánh'))
        contents = []
        if tran_van_chanh:
            contents = filter(lambda e: e.name != 'br', tran_van_chanh.parent.find_next_sibling('div').contents)
            contents = list(map(lambda e: e.strip(), contents))
            meaning['tran_van_chanh'] = contents

        # nguye_quoc_hung
        nguyen_quoc_hung = soup.find(string=re.compile('Từ điển Nguyễn Quốc Hùng'))
        contents = []
        if nguyen_quoc_hung:
            contents = filter(lambda e: e.name != 'br', nguyen_quoc_hung.parent.find_next_sibling('div').contents)
            contents = list(map(lambda e: e.strip(), contents))
            meaning['nguyen_quoc_hung'] = contents

        res.append(json.dumps(meaning, ensure_ascii=False))

        count = count + 1
        # if count == 3:
        #     break
    return res

data = get_char_meaning('../output1/characters.txt', '../hvdict/char_data')
f = open('../output1/characters_meaning.txt', 'w')
for line in data:
    f.write('{}\n'.format(line))
f.close

    
