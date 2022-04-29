#!/usr/bin/env python

import sys
import collections

caller_list = []

for line in sys.stdin:
    line = line.strip()

    caller_list.append(line)

counter = collections.Counter(caller_list)
maxList = counter.most_common(3)


for item in maxList:
    number = str(item[0])
    number = number.strip("' '")
    pretty_number = '(' + number[:3] + ') ' + number[3:6] + '-' + number[6:]
    print(pretty_number, "   ", item[1])
