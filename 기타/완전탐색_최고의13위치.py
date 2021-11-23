n = int(input())
grid = []
for _ in range(n):
    number = list(map(int,input().split()))

    grid.append(number)
#이 중에서 1x3 틀로 탐색 후 최대값 출력
# 0 0 0 1 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 0 1 0
# 0 0 0 1 1

# 동전 탐색 함수
def count_coin(row,start,end):

    number_coin = 0
    for col in range(start,end+1):
        number_coin += grid[row][col]
    return number_coin

maxima = 0
# 탐색할 장판
for row in range(n):
    for col in range(n):

        if col + 2  >= n :
            continue

        maxima = max(maxima,count_coin(row,col,col+2))

print(maxima)