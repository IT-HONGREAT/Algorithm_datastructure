M, N = list(map(int, input().split()))  # 세로, 가로


answer = 0
x, y = 0, 0

# 순서 명시
move_type = {
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1],
    "U": [-1, 0],
}


def get_next_direction(direction: str) -> str:
    next = ""
    if direction == "R":
        next = "D"
    if direction == "D":
        next = "L"
    if direction == "L":
        next = "U"
    if direction == "U":
        next = "R"
    return next


grid = []
for i in range(M):
    one_col = []
    for j in range(N):
        one_col.append("O")
    grid.append(one_col)
grid[0][0] = "X"
direction = "R"
exist_o = True
while exist_o:
    can_go = False
    v = move_type[direction]

    temp_next_x, temp_next_y = x + v[0], y + v[1]
    # print("grid", grid)
    if 0 <= temp_next_x < M and 0 <= temp_next_y < N and grid[temp_next_x][temp_next_y] != "X":
        can_go = True

    if not can_go:
        direction = get_next_direction(direction)
        v = move_type[direction]
        x, y = x + v[0], y + v[1]
        exist_o = False
        for i in grid:
            for j in i:
                if j == "O":
                    exist_o = True
        if exist_o == False:
            break
        answer += 1
        # print("turned!")
        grid[x][y] = "X"

    # 방향전환을 하지 않아도되는 조건 == 가도되는 조건
    if can_go:
        if grid[temp_next_x][temp_next_y] != "X":
            x, y = temp_next_x, temp_next_y
            grid[x][y] = "X"
        continue

print(answer)
