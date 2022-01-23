import sys

sys.stdin = open('input값 파일.txt', 'r')

N, L, K = map(int, input().split())  # 문제수,자신의난이도,문제개수제한

# 쉬운,어려운 문제
easy, hard = 0, 0

for _ in range(N):
    e, h = map(int, input().split())

    if h <= L:
        hard += 1
    elif e <= L:
        easy += 1

answer = min(hard, K) * 140

if hard < K:
    answer += (min(K - hard, easy) * 100)

print(answer)