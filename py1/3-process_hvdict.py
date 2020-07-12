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

def collect_phrases(html_file):
    res = OrderedDict()
    soup = BeautifulSoup(open(html_file), features="html.parser")
    p_strs = soup.find_all(string=re.compile('Từ ghép .*'))
    # if p_strs and len(p_strs) > 1:
    #     print(html_file)
    for p_str in p_strs:
        a_tags = p_str.parent.find_next('div').find_all('a')
        for a in a_tags:
            text = a.string
            lastsp = text.rfind(' ')
            phrase = text[lastsp+1:]
            meaning = text[0:lastsp]
            if not phrase in res:
                res[phrase] = []
            if not meaning in res[phrase]:
                res[phrase].append(meaning)
    return res

def collect_all_phrases(chars_path, data_folder):
    chars_no_data = OrderedSet()
    
    # collect phrases
    char_phrases = []
    f = open(chars_path)
    for line in f:
        char = line.strip()
        if not has_data(char, data_folder):
            chars_no_data.add(char)
        else: 
            phrases = collect_phrases(os.path.join(data_folder, char + '.html'))
            ch_phs = OrderedDict({'char':char, 'phrases': phrases})
            char_phrases.append(json.dumps(ch_phs, ensure_ascii=False))
    f.close()

    # write phrases
    print('total chars with phrases: {}'.format(len(char_phrases)))
    fo = open('../hvdict/char_phrases.txt', 'w')
    for cp in char_phrases:
        fo.write('{}\n'.format(cp))
    fo.close()

    # save characters without data
    print('characters without data: '.format(len(chars_no_data)))
    for char in chars_no_data:
        print(char)

# collect_all_phrases('../output1/characters.txt', '../hvdict/char_data')

def get_phrases_meanings(input, output):
    all_phrases = OrderedDict()
    f = open(input)
    for line in f:
        phrases = json.loads(line.strip(), object_pairs_hook=OrderedDict)['phrases']
        for key in phrases:
            if key not in all_phrases:
                all_phrases[key] = []
            for meaning in phrases[key]:
                if not meaning in all_phrases[key]:
                    all_phrases[key].append(meaning)
    f.close
    f = open(output, 'w')
    for ph in all_phrases:
        ph_meanings = OrderedDict({ph: all_phrases[ph]})
        f.write('{}\n'.format(json.dumps(ph_meanings, ensure_ascii=False)))
    f.close

# get_phrases_meanings('../hvdict/char_phrases.txt', '../hvdict/phrases_meanings.txt')

def get_phrases(input, output):
    all_phrases = OrderedSet()
    f = open(input)
    for line in f:
        phrase_meanings = json.loads(line.strip(), object_pairs_hook=OrderedDict)
        all_phrases.add(list(phrase_meanings.keys())[0])
    f.close
    f = open(output, 'w')
    for ph in all_phrases:
        f.write('{}\n'.format(ph))
    f.close

get_phrases('../hvdict/phrases_meanings.txt', '../hvdict/phrases.txt')
