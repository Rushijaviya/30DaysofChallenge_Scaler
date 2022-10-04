# The Full Counting Sort
# https://www.hackerrank.com/challenges/countingsort4/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    d=defaultdict(list)
    n=len(arr)
    x=n//2
    for i in range(x):
        arr[i][1]='-'
    for i in range(n):
        d[int(arr[i][0])].append(arr[i][1])
    ans=""
    for i in sorted(d):
        for i in d[i]:
            ans+=(i+' ')
    print(ans)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
