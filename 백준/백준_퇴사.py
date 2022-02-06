def solution(N, duration, cost):
    dp = [0] * (N + 1)

    def dynamic_programming():

        for i in range(N - 1, -1, -1):
            if duration[i] + i > N:
                dp[i] = dp[i + 1]
            else:
                dp[i] = max(dp[i + 1], cost[i] + dp[i + duration[i]])
            print(dp)
        return dp[0]

    result = dynamic_programming()
    return result


N = 7
duration = [3, 5, 1, 1, 2, 4, 2]
cost = [10, 20, 10, 20, 15, 40, 200]
print(solution(N, duration, cost))

N = 10
duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
print(solution(N, duration, cost))
