"""
철수는 개발자에서 은퇴하여 치킨집을 하게 되었다. 철수는 뛰어난 개발 실력으로 N대의 자동 튀김기를 만들어냈다. i번째 자동 튀김기는 치킨을 한 번 튀기는 데에 fry[i] 만큼의 시간이 걸리며, 튀김이 한번 끝나면 clean[i] 만큼의 시간동안 자동 세척을 한다.

철수가 C 번 치킨을 튀겨내려고 할 때, 최소한 몇 시간 동안 자동 튀김기를 가동해야 하는지 계산하시오.

제약 사항

0 < N <= 100000
fry[i]는 0 < fry[i] <= 100를 만족하는 정수
clean[i]는 0 < clean[i] <= 100를 만족하는 정수
0 < C <= 100000


N	fry	clean	C	return
2	[3, 6]	[2, 1]	20	58
4	[2, 2, 1, 3]	[2, 4, 3, 2]	2	2

"""


def solution(N, fry, clean, C):
    t = 0
    count_fry = 0
    for f, c in zip(fry, clean):
        count_fry += (mid + c) // (f + c)

    if count_fry >= C:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

    return 'line'


print(solution(2, [3, 6], [2, 1], 20))
print(solution(4, [2, 2, 1, 3], [2, 4, 3, 2], 2))
