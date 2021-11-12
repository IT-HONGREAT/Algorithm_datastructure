# 1 2 3 4 5 6 7 8  ascending
# 8 7 6 5 4 3 2 1  descending
# 8 1 7 2 6 3 5 4  mixed

n = list(map(int,input().split()))
ascending = True
descending = True

for i in range(1, 8):
    if n[i] > n[i-1]:
        descending = False
    elif n[i] < n[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')


