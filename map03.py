#!/usr/bin/env python

import sys
from collections import defaultdict

pls_dont_call = ['2166849356', '4049345110', '5893715037', '9457920329']

marked_list = set()
number_list = []
# number_list = {}
lines = []

for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    tokens = line.split(';')
    temp_unwant = tokens[3].strip()
    token = tokens[1].split(',')
    marketer = token[0]

    if temp_unwant in pls_dont_call:
        marked_list.add(marketer)

marked_list = list(marked_list)

for line in lines:
    tokens = line.split(';')
    cur_number = tokens[3].strip()
    temp_marketer = tokens[1].strip()

    if temp_marketer in marked_list:
        number_list.append(cur_number)
        # if cur_number in number_list:
        #     number_list[cur_number] += 1
        # else:
        #     number_list[cur_number] = 1

print(number_list)

