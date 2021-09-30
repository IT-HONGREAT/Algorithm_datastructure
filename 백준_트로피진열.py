# 5
# 1
# 2
# 3
# 4
# 5

n = int(input())

prizes_L = []

for _ in range(n):
    prize = int(input())
    prizes_L.append(prize)

prizes_R = prizes_L[::-1]

save_L = 0
save_R = 0

answer_L = []
answer_R = []

for l in prizes_L:
    if l > save_L:
        answer_L.append(l)

        save_L = l

for r in prizes_R:
    if r > save_R:
        answer_R.append(r)

        save_R = r

print(len(answer_L))
print(len(answer_R))
