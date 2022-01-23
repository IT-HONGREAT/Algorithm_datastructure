"""
입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
출력: True

입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
출력: False
"""
from itertools import combinations, permutations

str1_1 = "aabcc"
str1_2 = "dbbca"
str1_3 = "aadbbcbcac"

str2_1 = "aabcc"
str2_2 = "dbbca"
str2_3 = "aadbbbaccc"


def solution(s1, s2, s3):
    Target = s3
    all = [i for i in enumerate(s1)]+[i for i in enumerate(s2)]

    for i in permutations(all,len(s3)):
        print(i)
        # if "".join(i)==s3:
        #     return True

    return False
        # print("".join(i))



print(solution(str1_1, str1_2, str1_3))
print(solution(str2_1, str2_2, str2_3))

