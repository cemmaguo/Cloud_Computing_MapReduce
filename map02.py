#!/usr/bin/env python

import sys

pls_dont_call = ['2166849356', '4049345110', '5893715037', '9457920329']
telemarketers_dict = {}
marked_list = set()

for line in sys.stdin:
    line = line.strip()
    tokens = line.split(';')
    token = tokens[1].split(',')
    marketer = token[0]
    temp_unwant = tokens[3].strip()

    if marketer in telemarketers_dict:
        telemarketers_dict[marketer] += 1
    else:
        telemarketers_dict[marketer] = 1

    if temp_unwant in pls_dont_call:
        marked_list.add(marketer)
    
print(list(marked_list), '\t', telemarketers_dict)
