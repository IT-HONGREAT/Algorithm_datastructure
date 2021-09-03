def sosu(n):

    count = 3

    for i in range(1,n+1):
        if n % i == 0 :
            count -= 1

        if count == 0:
            return False
    if count == 1 :
        return True   #소수일때 true 참임.

answer = 0
turn = int(input())

a = list(map(int,input().split(" ")))

for i in range(turn):
    if sosu(a[i]):
        answer += 1

print(answer)