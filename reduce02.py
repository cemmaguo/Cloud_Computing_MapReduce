#!/usr/bin/env python

import sys
import ast

for line in sys.stdin:
    line = line.strip()
    # line = line.strip('[ ]')
    # line = line.replace('\"', '')
    # marked_list = line.split(',')
    marked_list, temp = line.split('\t', 1)
    marked_list = marked_list.strip('[ ]')
    temp = temp.strip()
    theDict = ast.literal_eval(temp)
    # marked_list = marked_list.strip('{ }')
    # marked_list = marked_list.split(',')
    # total = 0
    # count = 0
    for marketer, count in sorted(theDict.items(), reverse=False):
        # total += 1
        if marketer in marked_list:
            # count += 1
            print(marketer, count)


# print("total company: ", total)
# print("marked company: ", count)


