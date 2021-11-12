n,m = list(map(int,input().split()))
card = list(map(int,input().split()))

# print(n,m)

result = 0
end = len(card)

for i in range(end):
    for j in range(i+1, end):
        for k in range(j+1, end):
            total = card[i]+card[j]+card[k]
            if total <= m:
                result = max(result,total)

print(result)