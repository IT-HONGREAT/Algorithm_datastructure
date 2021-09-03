# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung
# 나이 순, 나이가 같으면 가입한 순

n = int(input())

test = []
for i in range(n):

    age, name = input().split(" ")
    test.append([age, name])

test.sort(key=lambda x:(x[0]))

for j in test:
    print(j[0],j[1])
