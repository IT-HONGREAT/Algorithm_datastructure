# 7
# 2 4
# 11 4
# 15 8
# 4 6
# 5 3
# 8 10
# 13 6

n = int(input())

array = []

for _ in range(n):
    x,y = map(int,input().strip().split())
    array.append((x,y))
array = sorted(array)

max_y_x = 0
max_y = 0
max_x = 0

for x,y in array:
    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y
        max_y_x = x

make_warehouse_x = [0] * (max_x + 1)

for x,y in array:
    make_warehouse_x[x] = y

answer = 0
sum_l = 0
sum_r = 0

for i in range(max_y_x + 1):
    if make_warehouse_x[i] > sum_l:
        sum_l = make_warehouse_x[i]
    answer += sum_l

for i in range(max_x,max_y_x,-1):
    if make_warehouse_x[i] > sum_r:
        sum_r = make_warehouse_x[i]
    answer += sum_r
print(answer)