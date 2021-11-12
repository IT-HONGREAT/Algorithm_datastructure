# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

n = int(input())

for _ in range(n):

    N,M = map(int,input().split())
    numbers = list(map(int,input().split()))
    q = [(i, idx) for idx, i in enumerate(numbers)]
    count = 0
    while True:
        if q[0][0] == max(q, key=lambda x:x[0])[0]:
            count += 1

            if q[0][1] == M:
                print(count)
                break
            else:
                q.pop(0)

        else:
            q.append(q.pop(0))




