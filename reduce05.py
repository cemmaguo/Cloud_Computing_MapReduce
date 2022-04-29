#!/usr/bin/env python

import sys
import collections

hour_list = []

for line in sys.stdin:
    line = line.strip()
    hour_list.append(line)

counter = collections.Counter(hour_list)
maxList = counter.most_common(3)

for item in maxList:
    hour = int(item[0])
    if hour < 12:
        pretty_hour = str(hour) + " a.m."
    else:
        pretty_hour = str(hour) + " p.m."
    
    print(pretty_hour, "   ", item[1])