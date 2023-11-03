import sys

# M: 세로, N: 가로, x: 현재 위치 x, y: 현재 위치 y, d: 바라보는 방향
M, N = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left(d):
    return (d - 1) % 4


def clean(x, y, d):
    global board
    count = 0
    turn_time = 0

    while True:
        if board[x][y] == 0:
            board[x][y] = 2  # 현재 위치를 청소함 (2로 표시)
            count += 1

        if turn_time < 4:
            d = turn_left(d)
            nx, ny = x + dx[d], y + dy[d]
            if board[nx][ny] == 0:
                x, y = nx, ny
                turn_time = 0
                continue
            else:
                turn_time += 1
        else:
            # 네 방향 모두 청소가 되어있거나 벽인 경우
            nx, ny = x - dx[d], y - dy[d]
            if board[nx][ny] == 2:
                x, y = nx, ny
                turn_time = 0
            else:
                # 뒤쪽 방향이 벽인 경우
                return count

    return count


print(clean(x, y, d))
