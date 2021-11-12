# 5
# 2 4 -10 4 -9

n = int(input())
save = []
numbers = list(map(int,input().split(" ")))

find_loc = sorted(set(numbers))

save = {}
for loc, num in enumerate(find_loc):
    save[num] = loc

for i in numbers:
    print(save[i],end=" ")