from itertools import product

n, m = map(int, input().split(" "))
nlist = [x for x in range(1, n + 1)]

# print(nlist)
for i in product(nlist, repeat=m):
     print(*i)