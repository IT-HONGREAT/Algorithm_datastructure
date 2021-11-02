# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    str = '#'
    for i in range(n):
        print(str.rjust(n))
        str += '#'

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
