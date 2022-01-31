import sys

sys.stdin = open('input값 파일.txt', 'r')
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

array = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# dp[i][j] = i,j 까지 왔을 때 가장 큰 정사각형,한 변의 길이 저장
# i,j 좌표에서 min_(하나라도 정사각형이 아니면 정사각형이 될 수 없다.)((i-1,j),(i,j-1),(i-1,j-1))+1 이고
# (i,j)가 1이라면 +1 해준다./ 0이라면 그냥 0
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for idx, j in enumerate(list(map(int, list(input())))):
        array[i + 1][idx + 1] = j

for i in range(N + 1):
    for j in range(M + 1):
        if array[i][j] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(max(max(i) for i in dp) ** 2)


"""
array = [[0 for _ in range(m)] for _ in range(n)]  # 한 줄(str) -> 리스트(한 줄씩)

for i in range(n):
    line = input()
    for j in range(m):
        array[i][j] = line[j]

# print(array)

visited = [[0 for _ in range(m)] for _ in range(n)]


def dfs(x, y, width_check):
    visited[x][y] = True
    w = width_check
    directions = [(w, 0), (0, w), (w, w)]

    for i, j in directions:
        nx, ny = x + i, y + j

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny,w)



while True:
    true_square = 0
    width_check = 1  # 확인 할 넓이 늘리기
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i,j,width_check)
                true_square = 1
                print(true_square)
        print(true_square,width_check)
    width_check += 1
    if true_square == 0:
        break
    print ((width_check + 1) ** 2)

# 1 4
# 2 9
# 3 16
# 4 25
"""
