from itertools import combinations

def solution(nums):
    new = []

    for i in combinations(nums, 3):

        new.append(i)

    sum = list(map(lambda x: x[0] + x[1] + x[2], new))
    answer = list(filter(lambda x: x % 2 != 0 and x % 3 != 0, sum))

    return len(answer)

print(solution([1,2,7,6,4]))
print(solution([1,2,36,3,4,5,6]))
