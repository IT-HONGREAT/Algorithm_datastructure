# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3
# 첫째 줄에 N, M(1 ≤ M ≤ 100,000)이 주어진다.
# 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)가 주어진다.
# 이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다.
from collections import deque

N, M = map(int,input().split())  # 섬의 개수 제한 , 다리의 정보

island = [[]for _ in range(N + 1)]

def bfs(c):
    queue = deque([start_node])

    visited = [False] * (N + 1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()
        for y, w in island[x]:
            if not visited[y] and w >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]


start = 1000000000
end = 1


for _ in range(M):
    x, y, w = map(int,input().split())  #섬 A, 섬 B, 다리중량제한 C

    island[x].append((y, w))
    island[y].append((x, w))
    start = min(start, w)
    end = max(end, w)

start_node,end_node = map(int,input().split())

result = start
while (start <= end):
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)