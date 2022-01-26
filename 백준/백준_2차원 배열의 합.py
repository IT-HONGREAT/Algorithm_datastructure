# 2 3
# 1 2 4
# 8 16 32
# 3
# 1 1 2 3
# 1 2 1 2
# 1 3 2 3

"""
첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다.
그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다.
다음 K개의 줄에는 네 개의 정수로 i, j, x, y
"""
import sys

sys.stdin = open('input값 파일.txt', 'r')

N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

K = int(input())


# 로직 : (x,y)까지의 부분합 - (i,j)까지의 부분합
def solution(position: list) -> int:
    i, j, x, y = position[0], position[1], position[2], position[3]
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    """
    부분합 로직
    문제예시와 같이 증가하는 (2,2) 행렬에서
    (2,2) = (1,2)+(2,1)-(1,1) 원리를 이용해서 dp 생성하기
    """
    for a in range(1, N + 1):
        for b in range(1, M + 1):
            dp[a][b] = dp[a - 1][b] + dp[a][b - 1] - dp[a - 1][b - 1] + array[a - 1][b - 1]
    # print(dp,i,j,x,y)
    answer = dp[x][y] - dp[i - 1][y] - dp[x][j - 1] + dp[i - 1][j - 1]

    return answer


for _ in range(K):
    print(solution(list(map(int, input().split()))))
