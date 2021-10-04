# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마

n = int(input())

count = 0
temp = 0
i = 1
while i <= n:

    if i <= n:
        n -= i
        count += 1
    i += 1

print(count)