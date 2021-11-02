# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mini = min(arr)
    maxi = max(arr)

    print(sum(arr) - maxi, sum(arr) - mini)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
