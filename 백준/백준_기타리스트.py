# 3 5 10
# 5 3 7
# return 10


n, s, m = map(int,input().split())
array = list(map(int,input().split()))

check = [ [0]*(m+1) for i in range(n + 1) ]
check[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if check[i-1][j] == 0:
            continue
        if j - array[i - 1] >= 0:
            check[i][j - array[i - 1]] = 1
        if j + array[i -1] <= m:
            check[i][j + array[i - 1]] = 1

result = -1
for i in range(m, -1, -1):

    if check[-1][i] == 1:
        result = i
        break
print(result)
