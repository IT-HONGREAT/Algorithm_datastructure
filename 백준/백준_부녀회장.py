import sys
def sosu(n):

    count = 3

    for i in range(1,n+1):
        if n % i == 0 :
            count -= 1

        if count == 0:
            return False
    if count == 1 :
        return True   #소수일때 true 참임.

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
answer_s = 0
answer_m = 0
for i in range(m,n+1):
    if sosu(i):
        answer_s+=i
    if sosu(i) and answer_m ==0:
        answer_m += i
if answer_m != 0:
    print(answer_s)
    print(answer_m)
else:
    print(-1)

