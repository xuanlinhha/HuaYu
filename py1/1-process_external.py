# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
from ordered_set import OrderedSet

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

# generate chars and phrases
def print_data(path, out=''):
    res = get_data(path)
    if out:
        f=open(out, 'w')
        for i in res:
            f.write('{}\n'.format(i))
        f.close
    else:
        for i in res:
            print(i)

# print_data('../ex-src/traditional-chars.txt', '../ex-src/characters.txt')
# print_data('../ex-src/cj5-ftzk_utf-8.txt', '../ex-src/phrases.txt')

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

# print_new_chars('../ex-src/characters.txt', '../ex-src/phrases.txt', '../ex-src/new_chars.txt')

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

rewrite('../ex-src/characters.txt')
