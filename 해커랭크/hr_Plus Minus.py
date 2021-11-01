# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

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
    count_plus = 0
    count_minus = 0
    count_zero = 0

    for i in arr:
        if i > 0:
            count_plus += 1
        elif i < 0:
            count_minus += 1
        elif i == 0:
            count_zero += 1

    plus = count_plus / len(arr)
    minus = count_minus / len(arr)
    zero = count_zero / len(arr)

    print("%0.6f" % float(plus))
    print("%0.6f" % float(minus))
    print("%0.6f" % float(zero))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
