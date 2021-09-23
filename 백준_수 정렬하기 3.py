# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    number = int(sys.stdin.readline())
    array[number] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)