# 2
# 'I am happy today'
# 'We want to win the first prize'


n = int(input())
for _ in range(n):
    a = list(map(str,input().split(" ")))
    print(*[x[::-1] for x in a])

