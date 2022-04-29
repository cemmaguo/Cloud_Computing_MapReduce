#!/usr/bin/env python

import sys
import ast
import collections

preMax_list = []
for line in sys.stdin:

    line = line.strip()
    num_list = line.split(',')
    counter = collections.Counter(num_list)

maxList = counter.most_common(3)

for item in maxList:
    number = str(item[0])
    number = number.strip("' '")
    pretty_number = '(' + number[:3] + ') ' + number[3:6] + '-' + number[6:]
    print(pretty_number, "   ", item[1])

# print(counter.most_common(3))
# print(num_list)
    # pre_dict = line
    # pre_dict = pre_dict.strip('[ ]')

    # number_dict = ast.literal_eval(pre_dict)



# for number in number_dict:
#     preMax_list.append(number_dict.get(number))

# preMax_list = list(set(preMax_list))
# max_list = sorted(preMax_list, reverse=True)[:3]

