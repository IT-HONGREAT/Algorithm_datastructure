import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):

    come = str(sys.stdin.readline())

    if 'push' in come:
        sep_num = come.split()
        number = sep_num[1]
        stack.append(int(number))

    if 'top' in come:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    if 'size' in come:
        print(len(stack))

    if 'pop' in come:
        if len(stack)>0:
            last_num = stack.pop()
            print(last_num)
        elif len(stack) == 0:
            print(-1)

    if 'empty' in come:
        if len(stack) == 0:
            print(1)
        else:
            print(0)



