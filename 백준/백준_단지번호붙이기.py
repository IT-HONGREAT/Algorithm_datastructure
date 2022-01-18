# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input())))


visited = [[False]*n for _ in range(n)]
homes = []
count_home = 0  #연결된 집 확인
def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    global count_home
    count_home += 1

    for i, j in directions:
        nx, ny = x + i, y + j

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if grid[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)



total_danji = 0  # dfs시행횟수 저장

for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            count_home = 0
            dfs(i, j)
            total_danji += 1
            homes.append(count_home)


# print(grid,visited)
# print(homes)
print(total_danji)
if homes:
    for i in homes:
        print(i)

