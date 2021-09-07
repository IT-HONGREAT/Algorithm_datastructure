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
answer = []

for i in range(1,n+1):
    input_num = int(input())
    while count <= input_num:
        print('while',count)
        stack.append(count)
        count += 1
        answer.append("+")
    if stack[-1] == input_num:
        stack.pop()
        answer.append('-1')
    else:
        print("NO")
    print(answer,stack,count)