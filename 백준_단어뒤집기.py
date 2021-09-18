# 2
# I am happy today
# We want to win the first prize


n = int(input())
for _ in range(n):
    word = input()
    word += " "
    stack = []
    for i in word:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(),end="")
            print(" ")