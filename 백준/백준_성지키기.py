"""
4 4             return 4
....
....
....
....

3 5             return 0
XX...
.XX..
...XX


5 8             return 3
....XXXX
........
XX.X.XX.
........
........
"""


N, M = map(int,input().split())

array = []

for _ in range(N):
    status = input()
    array.append(status)

count_row = 0
for row in array:
    check_row = 0
    for col in row:
        if col == 'X':
            check_row +=1

    if check_row ==0:
        count_row += 1

count_col = 0
for col in range(len(array[0])):
    check_col = 0
    for row in array:
        if row[col] == 'X':
            check_col += 1
    if check_col == 0:
        count_col +=1

print(max(count_row,count_col))