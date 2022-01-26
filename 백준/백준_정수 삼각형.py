# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# dp1
"""
n = int(input())
d = []

for i in range(n):
    d.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j] + d[i-1][j]
        elif j == len(d[i])-1:
            d[i][j] = d[i][j] + d[i-1][j-1]
        else:
            d[i][j] = d[i][j] +max(d[i-1][j-1],d[i-1][j])

# print(d)
print(max(d[n-1]))
"""
# dp2 가독성 좋게 구현_2차원배열dp
import sys

sys.stdin = open('input값 파일.txt', 'r')

n = int(input())
tri = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    for j in range(1, i + 1):
        tri[i][j] = line[j - 1]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]  #상위의 좌,우 중에 큰값에 더해주기

# print(dp)
print(max(dp[-1]))