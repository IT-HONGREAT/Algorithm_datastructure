from itertools import combinations

n, m = map(int, input().split(" "))
numbers = list(map(int, input().split()))

answer = []
for i in combinations(numbers, 3):
    print(i)
    if sum(i) <= 500:
        answer.append(sum(i))

print(max(answer))
