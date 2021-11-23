n = int(input())
grid = []
for _ in range(n):
    number = list(map(int,input().split()))

    grid.append(number)

#이 중에서 3x3 틀로 탐색 후 최대값 출력
# 0 0 0 1 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 0 1 0
# 0 0 0 1 1

#조건이 주어지지않은 전체 탐색 기능
def count_coin(row_start,row_end,col_start,col_end):

    count = 0
    for i in range(row_start, row_end+1):
        for j in range(col_start, col_end+1):

            count += grid[i][j]
    return count

answer = 0
#내부적으로 조건 조치함
for row in range(n):
    for col in range(n):


        if row + 2 >= n or col + 2 >= n:
            continue

        answer = max(answer,count_coin(row,row+2,col,col+2))

print(answer)
