import sys

sys.stdin = open('input값 파일.txt', 'r')

D = int(input())

dp = [1] + [0] * 7  # 정보과학관이 0번인덱스
print(dp)
"""
0 - 정보과학관
1 - 전산관
2 - 미래관
3 - 신양관
4 - 진리관
5 - 한경직관
6 - 학생회관
7 - 형남공학관
"""


def check_next(node):
    temp = [0 for _ in range(8)]
    temp[0] = node[1] + node[2]
    temp[1] = node[0] + node[3] + node[2]
    temp[2] = node[0] + node[1] + node[3] + node[5]
    temp[3] = node[1] + node[2] + node[4] + node[5]
    temp[4] = node[3] + node[5] + node[6]
    temp[5] = node[2] + node[3] + node[4] + node[7]
    temp[6] = node[4] + node[7]
    temp[7] = node[5] + node[6]

    return temp

for _ in range(D):
    dp = check_next(dp)

print(dp[0]%1000000007)