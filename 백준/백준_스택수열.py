# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

n = int(input())

count = 1
stack = []
result = []


for i in range(1, n+1):
    number = int(input())
    while count <= number:
        stack.append(count)
        count += 1
        result.append('+')

    if stack[-1] == number:
        stack.pop()
    else:
        print('NO')

print(result)

