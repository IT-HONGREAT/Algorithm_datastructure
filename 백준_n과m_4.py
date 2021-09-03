from itertools import combinations_with_replacement as cr

n, m = map(int, input().split(" "))
nlist = [x for x in range(1, n + 1)]

print(nlist)
for i in cr(nlist, m):
    print(*i)
