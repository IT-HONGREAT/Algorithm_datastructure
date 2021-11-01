# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    c_a, c_b = 0, 0

    for i, j in zip(a, b):
        if i > j:
            c_a += 1
        elif j > i:
            c_b += 1

    return c_a, c_b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
