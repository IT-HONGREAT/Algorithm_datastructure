# https://leetcode.com/problems/find-the-town-judge/submissions/


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        if n == 1:
            return 1

        check = [[] for _ in range(n + 1)]

        for a, b in trust:
            check[b].append(a)

        # print('check',check)
        for idx, trusted in enumerate(check):

            if len(trusted) == n - 1:

                for pansa_check in check:
                    if idx in pansa_check:
                        return -1
                return idx

        return -1

test = Solution()

print(test.findJudge(2,	[[1,2]]	))
print(test.findJudge(3,	[[1,3],[2,3]]	))
print(test.findJudge(3,	[[1,3],[2,3],[3,1]]	))
print(test.findJudge(3,	[[1,2],[2,3]]	))
print(test.findJudge(4,	[[1,3],[1,4],[2,3],[2,4],[4,3]]))

