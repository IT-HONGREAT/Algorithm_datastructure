# n	vertex	                                                    return
# 6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
# [0,1] 인덱스가 간선으로 연결되어 있는 노드이고, 가장 멀리있는 노드가 어떤 것인지 탐색
# bfs 활용

from collections import deque

# 2. 그래프탐색
def bfs(start_node, visited, adj):
    count = 0
    q = deque([[start_node,count]])
    # q = [[start_node,count]]

    while q:
        # print(q)
        value = q.popleft()   # 반복되는 과정에서 팝
        # value = q.pop(0)
        start_node = value[0]   # 반복되는 과정에서 탐색시작점 갱신
        count = value[1]        # 반복되는 과정에서 count 갱신
        """
        visited를 의 각 인덱스를 노드라고 생각한다. 1번째 인덱스가 1번노드.
        """
        if visited[start_node] == -1:  #방문하지않은 경우 탐색한다. 방문한경우는 필요없음.
            visited[start_node] = count
            count += 1
            for e in adj[start_node]:  # 간선연결확인리스트
                """
                각 인덱스 번호의 리스트들이 연결된 [노드번호, count]를 q에 넣어준다.
                """
                q.append([e, count])
                # print(q)
        print('visited',visited,q)
    # return q
# print(bfs(1,[-1] * (6 + 1),[[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]))

def solution(n, edge):
    answer = 0

    visited = [-1] * (n + 1)
    # 1. 간선정의
    adj = [[] for _ in range(n+1)]

    for e in edge:
        x, y = e
        adj[x].append(y)
        adj[y].append(x)
    print('adj:',adj)
    bfs(1, visited, adj)

    #최대가 몇인지 확인
    for value in visited:
        if value == max(visited):
            answer += 1

    return answer
    # return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))