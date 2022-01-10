# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t


n = int(input())

def keylog(string):

    l_stack = []
    r_stack = []

    for word in string:
        if word == '-':
            if l_stack:
                l_stack.pop()
        elif word == '<':
            if l_stack:
                r_stack.append(l_stack.pop())

        elif word == '>':
            if r_stack:
                l_stack.append(r_stack.pop())

        else:
            l_stack.append(word)

    l_stack.extend(reversed(r_stack))

    return ''.join(l_stack)

for _ in range(n):
    print(keylog(input()))