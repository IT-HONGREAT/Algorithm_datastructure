from itertools import combinations


def solution(nums):
    answer = 0

    get_pockemon = len(nums) / 2
    kinds = len(list(set(nums)))

    if get_pockemon < kinds:
        return get_pockemon
    else:
        return kinds


print(solution([3,3,3,2,2,4]))
print(solution([3,1,2,3]))
print(solution([1,1]))
print(solution([1,4]))
print(solution([1,2,2,3,3,4]))