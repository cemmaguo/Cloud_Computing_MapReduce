#!/usr/bin/env python

import sys
import operator

telemarketers_dict = {}

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('\t')
    token = tokens[0].split(',')
    marketer = token[0]
    
    if marketer in telemarketers_dict:
        telemarketers_dict[marketer] += 1
    else:
        telemarketers_dict[marketer] = 1
    
for marketer, count in sorted(telemarketers_dict.items(), reverse=False):
    print(marketer, count)