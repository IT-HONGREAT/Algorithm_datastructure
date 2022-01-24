import sys

sys.stdin = open('input값 파일.txt', 'r')

C, M = [0, 0, 0], [0, 0, 0]
for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    now = i % 3
    aft = (i + 1) % 3

    M[now], M[aft] = max(M[now] - (C[aft] - M[aft]), 0), min(C[aft], M[aft] + M[now])

for i in M:
    print(i)
