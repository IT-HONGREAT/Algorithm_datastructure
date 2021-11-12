# [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5

from collections import Counter

def solution(clothes):

    kind = [i[1] for i in clothes]

    # print(Counter(kind))
    # print(len(Counter(kind)))
    result = 1
    for i in Counter(kind).values():
        # print(i)
        result *= (i+1)

    return result - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))