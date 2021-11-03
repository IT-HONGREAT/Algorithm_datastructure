# https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final = []
    for i in grades:
        one = i + 1
        two = i + 2
        if one % 5 == 0 and one >= 40:
            final.append(one)
        elif two % 5 == 0 and two >= 40:
            final.append(two)
        elif i + 2 < 40:
            final.append(i)
        else:
            final.append(i)

    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
