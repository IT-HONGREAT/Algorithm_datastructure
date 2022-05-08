# n	results	                                    return
# 5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2


from collections import defaultdict

def solution(n, results):
    answer = 0


    win_graph = defaultdict(set)  # 이긴 애들
    lose_graph = defaultdict(set)  # 진 애들

    for winner, loser in results:  # 결과에서 이기고 진 애들 그래프화
        win_graph[loser].add(winner)   # 진 사람이 key, 이긴 사람이 value
        lose_graph[winner].add(loser)  # 이 긴사람이 key, 진 사람이 value

    for idx in range(1,n+1):

        for winner in win_graph[idx]:
            lose_graph[winner].update(lose_graph[idx])
            # print('w',lose_graph)
        for loser in lose_graph[idx]:
            win_graph[loser].update(win_graph[idx])
            # print('l',win_graph)

    for i in range(1, n + 1):
        
        if len(win_graph[i]) + len(lose_graph[i]) == n - 1:  # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))