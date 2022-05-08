import sys

sys.stdin = open('input값 파일.txt', 'r')

n, array = int(input()), list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
