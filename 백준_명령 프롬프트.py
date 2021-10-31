# 3
# config.sys
# config.inf
# configures

n = int(input())
first = list(input())

array = []
for i in range(n-1):
    new = list(input())
    for j in range(len(first)):
        if first[j] != new[j]:
            # print(first[j])
            # first.replace(first[j],"?")
            first[j] = '?'

print(''.join(first))