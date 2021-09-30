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




#함수로 최적화_시도
n = int(input())

def find(list):

    now = list[0]
    result = 1
    for i in range(1,len(list)):
        if now < list[i]:
            result += 1
            now = list[i]
    return result

prizes_L= []
for i in range(n):
    prize = int(input())
    prizes_L.append(prize)

prizes_R = prizes_L[::-1]

print(find(prizes_L))
print(find(prizes_R))
