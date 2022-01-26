# 10
# 1 100 2 50 60 3 5 6 7 8
import sys

sys.stdin = open('input값 파일.txt', 'r')

n = int(input())
array = list(map(int, input().split()))

dp = array[:]

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(array[i] + dp[j] , dp[i])
print(max(dp))

