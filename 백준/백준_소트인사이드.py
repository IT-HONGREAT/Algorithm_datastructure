# 2143

numbers = input()

for i in range(9,-1,-1):
    for j in numbers:
        if i == int(j):
            print(i,end="")

