def sosu(n):

    count = 3

    for i in range(1,n+1):
        if n % i == 0 :
            count -= 1

        if count == 0:
            return False
    if count == 1 :
        return True   #소수일때 true 참임.

start = int(input())
end = int(input())

answer = []

for i in range(start, end+1):
    if sosu(i):
        answer.append(i)

print(sum(answer))
print(min(answer))
