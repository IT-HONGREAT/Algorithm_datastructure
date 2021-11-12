#4 2

# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3
from itertools import permutations

n, m = map(int,input().split(" "))

nlist = [x for x in range(1,n+1)]

answer = []
for i in permutations(nlist,m):
    answer.append(i)

for i in answer:
    print(*i)
