#!/usr/bin/env python

import sys

pls_dont_call = ['2166849356', '4049345110', '5893715037', '9457920329']

for line in sys.stdin:
    line = line.strip()
    tokens = line.split(';')
    temp_unwant = tokens[3].strip()

    if temp_unwant in pls_dont_call:
        print("{token}\t".format(token=tokens[1]))

        