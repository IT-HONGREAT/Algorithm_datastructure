# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l_to_r = 0
    r_to_l = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                l_to_r += arr[i][j]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j + i == len(arr) - 1:
                r_to_l += arr[i][j]

    return abs(l_to_r - r_to_l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
