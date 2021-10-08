# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# 물품의 수 N, 최대무게 K
# 물건의 무게 W, 물건의 가치 V

n, k = map(int, input().split())

item = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = map(int,input().split())

    for j in range(1, k + 1):
        if j < w:
            item[i][j] = item[i-1][j]
        else:
            item[i][j] = max(item[i-1][j], item[i-1][j-w] + v)


print(item[n][k])

