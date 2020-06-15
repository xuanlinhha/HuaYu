# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import time
import json
import os
from ordered_set import OrderedSet

def get_phrases_from_ext_dict(path):
    phrases = OrderedSet()
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        phrases.add(line.strip())
    return phrases

def get_phrases_from_hvdict(path):
    phrases = OrderedSet()
    f = open(path)
    lines = f.readlines()
    f.close()
    for line in lines:
        d = json.loads(line.strip())
        for phrase in d['phrases']:
            phrases.add(phrase)
    return phrases

def run():
    ex_dict_phrases = get_phrases_from_ext_dict('../output/TRADITIONAL_PHRASES.TXT')
    hvdict_phrases = get_phrases_from_hvdict('../output/TRADITIONAL_CHAR_PHRASES.TXT')
    print('len(ex_dict_phrases) = {}'.format(len(ex_dict_phrases)))
    print('len(hvdict_phrases) = {}'.format(len(hvdict_phrases)))
    new_phrases = OrderedSet()
    for p in hvdict_phrases:
        if p not in ex_dict_phrases:
            new_phrases.add(p)
            ex_dict_phrases.add(p)
    print('len(new_phrases) = {}'.format(len(new_phrases)))
    print('len(ex_dict_phrases) = {}'.format(len(ex_dict_phrases)))
    # combine phrases
    f = open('../output/TRADITIONAL_COMBINED_PHRASES.TXT', 'w')
    for cp in ex_dict_phrases:
        f.writelines("%s\n" % cp)
    f.close()

run()