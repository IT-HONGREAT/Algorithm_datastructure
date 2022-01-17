import sys

sys.setrecursionlimit(100000)  # 재귀제한상향


# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트 케이스에 대해
# 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50),
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, j in directions:
        nx, ny = x + i, y + j
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if bat[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

    # 입력받고 바로 출력


for _ in range(int(input())):
    m, n, k = map(int, input().split())

    bat = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        bat[x][y] = 1

    answer = 0  # dfs시행횟수 저장
    for i in range(n):
        for j in range(m):
            if bat[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    # print(visited)
    print(answer)
