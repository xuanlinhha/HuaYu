# !/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
from ordered_set import OrderedSet

patt = '[a-z]+ +(.+)'

def convert(src, dest):
    f = open(src, encoding='gbk', errors='ignore')
    content = f.read()
    f.close()
    nf = open(dest, 'w', encoding='utf-8')
    nf.write(content)
    nf.close()

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

def extract_phrases(path):
    # input file
    f = open(path)
    lines = f.readlines()
    f.close()
    print('total line in {}: {}'.format(path, len(lines)))
    # process input
    phrases = OrderedSet()
    for line in lines:
        els = line.split(' ')[1].split('.')
        for e in els:
            phrases.add(e.replace('，', '').strip())
    return phrases

def extract_new_chars_from_phrases(phrases):
    old_chars = get_chars('../output/TRADITIONAL_CHARS.TXT')
    new_chars = OrderedSet()
    for phrase in phrases:
        for char in phrase:
            if char not in old_chars:
                new_chars.add(char)
    # write new chars
    for c in new_chars:
        print(c)

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

def extract_phrases_without_new_chars():
    chars = get_chars('../output/TRADITIONAL_CHARS.TXT')
    phrases = extract_phrases('../ex-src/cj5-ftzk_utf-8.txt')
    phrases_without_new_chars = OrderedSet()
    phrases_with_new_chars = OrderedSet()
    for phrase in phrases:
        has_new = False
        for char in phrase:
            if char not in chars:
                has_new = True
                break
        if has_new:
            phrases_with_new_chars.add(phrase)
        else:
            phrases_without_new_chars.add(phrase)
    print('total phrases = {}'.format(len(phrases)))
    print('phrases without new chars = {}'.format(len(phrases_without_new_chars)))
    print('phrases with new chars = {}'.format(len(phrases_with_new_chars)))
    f = open('../output/TRADITIONAL_PHRASES.TXT', 'w')
    for p in phrases_without_new_chars:
        f.write('%s\n' % p)
    f.close()
    print('Phrases with new chars:')
    for p in phrases_with_new_chars:
        print(p)

def run():
    # convert('../ex-src/cj5-ftzk.txt', '../ex-src/cj5-ftzk_utf-8.txt')
    # phrases = extract_phrases('../ex-src/cj5-ftzk_utf-8.txt')
    # extract_new_chars_from_phrases(phrases)
    # extract_new_chars_from_file('tmp.txt')
    extract_phrases_without_new_chars()

run()
