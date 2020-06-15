# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re
from ordered_set import OrderedSet

patt = '[a-z]+ +(.+)'
def get_chars_from_ex_data(src, dest):
    # get chars
    chars = OrderedSet()
    with open(src) as f:
        for line in f:
            m = re.search(patt, line)
            if m:
                chars.add(m.group(1))

    # write chars
    with open(dest, 'w') as of:
        for char in chars:
            of.write('%s\n' % char)
    print(len(chars))

def run():
    get_chars_from_ex_data('../ex-src/traditional-chars.txt', '../output/TRADITIONAL_CHARS.TXT')

run()
