# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
from collections import deque

N, M, V = map(int, input().split())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    node_a, node_b = map(int,input().split())
    adj[node_a].append(node_b)
    adj[node_b].append(node_a)

for i in adj:
    i.sort()

visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

def dfs(node):
    print(node,end=' ')
    visited_dfs[node] = True

    for check in adj[node]:
        if not (visited_dfs[check]):
            dfs(check)

def bfs(node):
    q = deque([node])

    while q:
        node = q.popleft()
        if not(visited_bfs[node]):
            visited_bfs[node] = True

            print(node,end=' ')

            for check in adj[node]:
                if not (visited_bfs[check]):
                    q.append(check)



dfs(V)
bfs(V)




print(adj)
