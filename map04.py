#!/usr/bin/env python

import sys

pls_dont_call = ['2166849356', '4049345110', '5893715037', '9457920329']
lines = []
marked_list = []

for line in sys.stdin:
    line = line.strip()
    lines.append(line)
    tokens = line.split(';')
    temp_unwant = tokens[3].strip()

    if temp_unwant in pls_dont_call:
        marked_list.append(tokens[1])

for line in lines:
    tokens = line.split(';')

    if tokens[1] in marked_list:
        print(tokens[2])