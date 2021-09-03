from itertools import combinations

n, m = map(int,input().split(" "))

nlist = [x for x in range(1,n+1)]

for i in combinations(nlist,m):
    print(*i)