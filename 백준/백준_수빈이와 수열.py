import sys
sys.stdin = open('input값 파일.txt','r')

#input
# 4
# 3 2 3 5
#input2
# 5
# 1 2 2 3 4

n = int(input())
numbers = list(map(int,input().split()))
origin = []
for i in range(n):

    aftersum = numbers[i] * (i+1)
    origin_number = aftersum - sum(origin[:i+1])
    origin.append(origin_number)

print(*origin)