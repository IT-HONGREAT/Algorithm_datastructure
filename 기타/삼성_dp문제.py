"""
1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.
상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다.
2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.
또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
"""


def solution(N, duration, cost):
    # 불가능한 스케줄은 삭제, 코스트 0 처리
    for idx in range(N):
        if duration[idx] + idx > N:
            duration[idx], cost[idx] = 0, 0

    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    # dp[i][j]
    check = 0
    for i in range(N - 1, -1, -1):
        for j in range(i, -1, -1):

            for k in range():

    print(check)

    print(cost)
    print(dp)
    return 0


N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))

# N = 10
# duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
# print(solution(N, duration, cost))
