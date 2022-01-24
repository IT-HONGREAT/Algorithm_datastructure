"""
입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
출력: True

입력: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
출력: False
"""
str1_1 = "aabcc"
str1_2 = "dbbca"
str1_3 = "aadbbcbcac"

str2_1 = "aabcc"
str2_2 = "dbbca"
str2_3 = "aadbbbaccc"


def solution(s1, s2, s3):
    length1, length2, length3 = len(s1), len(s2), len(s3)

    dp = [[True for _ in range(length2 + 1)] for _ in range(length1 + 1)]
    # print(dp)
    for i in range(1, length1 + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for i in range(1, length2 + 1):
        # print(dp)
        dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]
    #     print()
    # print(dp)

    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
    # print(dp)
    return dp[-1][-1]


print(solution(str1_1, str1_2, str1_3))
print(solution(str2_1, str2_2, str2_3))
