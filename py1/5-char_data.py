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

def get_char_data(chars_src, data_folder):
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
        
        data = OrderedDict()
        data['char'] = char

        parent = soup.find(string=re.compile('Unicode: .*')).parent
        # han viet
        han_viet_ele = parent.find(string=re.compile('Âm Hán Việt: .*'))
        han_viet = []
        if han_viet_ele:
            for sp in find_next_siblings(han_viet_ele, 'span'):
                han_viet.append(sp.string)
        data['han_viet'] = han_viet
        # pinyin
        pinyin_ele = parent.find(string=re.compile('Âm Pinyin: .*'))
        pinyin = []
        for a in find_next_siblings(pinyin_ele, 'a'):
            pinyin.append(a.string)
        data['pinyin'] = pinyin
        # nom
        nom_ele = parent.find(string=re.compile('Âm Nôm: .*'))
        nom = []
        for a in find_next_siblings(nom_ele, 'a'):
            nom.append(a.string)
        data['nom'] = nom
        # unicode
        unicode_ele = parent.find(string=re.compile('Unicode: .*'))
        code = find_next_siblings(unicode_ele, 'a')[0].string
        data['unicode'] = code
        # tong net
        tong_net = parent.find(string=re.compile('Tổng nét: .*')).split(': ')[1]
        data['tong_net'] = tong_net
        # bo
        bo_ele = parent.find(string=re.compile('Bộ: .*'))
        bo = []
        for a in find_next_siblings(bo_ele, 'a'):
            bo.append(a.string + a.next_sibling)
        data['bo'] = bo
        # luc_thu
        luc_thu_ele = parent.find(string=re.compile('Lục thư: .*'))
        luc_thu = []
        if luc_thu_ele:
            luc_thu.append(luc_thu_ele.split(': ')[1])
        data['luc_thu'] = luc_thu
        # hinh thai
        hinh_thai_ele = parent.find(string=re.compile('Hình thái: .*'))
        hinh_thai = []
        if hinh_thai_ele:
            hinh_thai.append(hinh_thai_ele.split(': ')[1])
            for a in find_next_siblings(hinh_thai_ele, 'a'):
                hinh_thai.append(a.string)
        data['hinh_thai'] = hinh_thai
        # net but
        net_but_ele = parent.find(string=re.compile('Nét bút: .*'))
        net_but = []
        for a in find_next_siblings(net_but_ele, 'a'):
            net_but.append(a.string)
        data['net_but'] = net_but
        # thong dung
        han_co_thong_dung = parent.find(string=re.compile('Độ thông dụng trong Hán ngữ cổ: .*')).split(': ')[1]
        data['han_co_thong_dung'] = han_co_thong_dung
        hien_dai_thong_dung = parent.find(string=re.compile('Độ thông dụng trong tiếng Trung hiện đại: .*')).split(': ')[1]
        data['hien_dai_thong_dung'] = hien_dai_thong_dung

        # di the
        di_the = []
        anchor = soup.find(string=re.compile('Dị thể .*'))
        if anchor:
            spans = anchor.parent.find_next_sibling('div').find_all('span')
            for sp in spans:
                tmp = os.path.basename(sp.parent['href'])
                if tmp in chars:
                    di_the.append(tmp)
        data['di_the'] = di_the

        res.append(json.dumps(data, ensure_ascii=False))
        
        count = count + 1
        # if count == 3:
        #     break
    return res

def find_next_siblings(start, tag_name):
    if not start:
        return []
    res = []
    tmp = start.next_sibling
    while tmp and tmp.name != 'br':
        if tmp.name == tag_name:
            res.append(tmp)
        tmp = tmp.next_sibling
    return res

data = get_char_data('../output1/characters.txt', '../hvdict/char_data')
f = open('../output1/characters_data.txt', 'w')
for line in data:
    f.write('{}\n'.format(line))
f.close

    
