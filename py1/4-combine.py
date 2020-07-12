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

# get new chars
def print_new_chars(src1, src2, out=''):
    chars = get_data(src1)
    phrases = get_data(src2)
    new_chars = OrderedSet()
    for p in phrases:
        for c in p:
            if not c in chars:
                new_chars.add(c)
    if out:
        f=open(out, 'w')
        for i in new_chars:
            f.write('{}\n'.format(i))
        f.close
    else:
        for i in new_chars:
            print(i)

# print_new_chars('../ex-src/characters.txt', '../hvdict/phrases.txt', '../hvdict/new_chars.txt')

def rewrite(path):
    lines = OrderedSet()
    # read
    f = open(path)
    for line in f:
        lines.add(line.strip())
    f.close
    # write
    f = open(path, 'w')
    for line in lines:
        f.write('{}\n'.format(line))
    f.close

# rewrite('../output1/characters.txt')
# print_new_chars('../output1/characters.txt', '../hvdict/phrases.txt', '../hvdict/new_chars.txt')

def remove_simplified_phrases(src1, src2, out=''):
    chars = get_data(src1)
    phrases = get_data(src2)
    res = OrderedSet()
    for p in phrases:
        has_simplified = False
        for c in p:
            if not c in chars:
                has_simplified = True
        if not has_simplified:
            res.add(p)
    if out:
        f=open(out, 'w')
        for i in res:
            f.write('{}\n'.format(i))
        f.close
    else:
        for i in res:
            print(i)

# remove_simplified_phrases('../output1/characters.txt', '../hvdict/phrases.txt', '../hvdict/filtered_phrases.txt')

def combine_phrases(src1, src2, out):
    phrases1 = get_data(src1)
    phrases2 = get_data(src2)
    for p in phrases2:
        phrases1.add(p)
    if out:
        f=open(out, 'w')
        for i in phrases1:
            f.write('{}\n'.format(i))
        f.close
    else:
        for i in phrases1:
            print(i)

# combine_phrases('../ex-src/phrases.txt', '../hvdict/filtered_phrases.txt', '../output1/phrases.txt')