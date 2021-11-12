# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 11 11
# 2 13
# 12 14

n = int(input())

record = []
check = [-1]

for _ in range(n):
    n,m = map(int,input().split())

    record.append([n,m])
record.sort()
print(record)
