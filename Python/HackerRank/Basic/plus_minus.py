#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_cnt = 0
    neg_cnt = 0
    zero_cnt = 0
    total = len(arr)
    for i in range(total):
        if arr[i]>0:
            pos_cnt+=1
        elif arr[i]<0:
            neg_cnt+=1
        else:
            zero_cnt+=1
    print(round(pos_cnt/total,6))
    print(round(neg_cnt/total,6))
    print(round(zero_cnt/total,6))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)