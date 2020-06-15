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

def get_map(path1, path2):
    mapping = {}
    f1 = open(path1)
    lines1 = f1.readlines()
    f1.close()
    f2 = open(path2)
    lines2 = f2.readlines()
    f2.close()
    print('len(lines1) = {}'.format(len(lines1)))
    print('len(lines2) = {}'.format(len(lines2)))
    for i in range(0, len(lines1)):
        if lines1[i].strip():
            mapping[lines1[i].strip()] = lines2[i].strip()
    return mapping

def rewrite_phrases(path):
    chars = get_chars('../output/TRADITIONAL_CHARS.TXT')
    mapping = get_map('newcps.txt', 'newcps_converted.txt')
    print('len(mapping) = {}'.format(len(mapping)))
    f = open(path)
    lines = f.readlines()
    f.close()
    new_char_phrases = []
    for line in lines:
        d = json.loads(line.strip())
        new_pharases = {}
        for phrase in d['phrases']:
            has_new = False
            for char in phrase:
                if char not in chars:
                    has_new = True
                    break
            if not has_new:
                new_pharases[phrase.replace('，', '')] = d['phrases'][phrase].replace('，', '')
            else:
                if phrase in mapping:
                    new_pharases[mapping[phrase].replace('，', '')] = d['phrases'][phrase].replace('，', '')
                else:
                    print('new phrase: "{}" not in map'.format(phrase))

        # new phrases
        for np in new_pharases:
            new_pharases[np] = new_pharases[np]
        new_char_phrases.append(json.dumps({'char':d['char'], 'phrases': new_pharases}, ensure_ascii=False))

    # write
    print('len(new_char_phrases) = {}'.format(len(new_char_phrases)))
    f = open('../output/TRADITIONAL_CHAR_PHRASES.TXT', 'w')
    for cp in new_char_phrases:
        f.writelines("%s\n" % cp)
    f.close()

def run():
    rewrite_phrases('../output/ONLINE_CHAR_PHRASES.TXT')

run()
