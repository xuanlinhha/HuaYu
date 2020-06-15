# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
import json
from ordered_set import OrderedSet

def get_chars(path):
    # check
    chars = OrderedSet()
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        for char in line.strip():
            chars.add(char)
    return chars

def extract_new_chars_from_scraped_data(path):
    old_chars = get_chars('../output/TRADITIONAL_CHARS.TXT')
    print('len(old_chars)={}'.format(len(old_chars)))
    new_chars = OrderedSet()
    phrases_with_new_chars = OrderedSet()
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        d = json.loads(line.strip())
        # print(d['char'])
        for phrase in d['phrases']:
            is_new = False
            for char in phrase:
                if char not in old_chars:
                	is_new = True
                	new_chars.add(char)
            if is_new:
                phrases_with_new_chars.add(phrase)

    for char in new_chars:
        print(char)
    print('\n================\n')
    for phrase in phrases_with_new_chars:
        print(phrase)

def extract_new_chars_from_file(path):
    old_chars = get_chars('../output/TRADITIONAL_CHARS.TXT')
    new_chars = OrderedSet()
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        for char in line.strip():
            if char not in old_chars:
                new_chars.add(char)
    # write not in chars
    for c in new_chars:
        print(c)

# extract_new_chars_from_scraped_data('../output/ONLINE_CHAR_PHRASES.TXT')
extract_new_chars_from_scraped_data('../output/TRADITIONAL_CHAR_PHRASES.TXT')
# extract_new_chars_from_file('tmp.txt')