# 5 17

import sys
import collections
input = sys.stdin.readline

N, K = map(int,input().split()) # 수빈이와 동생 위치 입력 받기
queue = collections.deque() # bfs를 위한 queue 생성

queue.append(N) # 시작 지점 N
dist = collections.defaultdict(int) # 시간초 정보를 담을 dic
visited = collections.defaultdict(int) # 방문 정점을 기록할 dic
visited[N] = 1 # 시작 지점 방문

# bfs
while queue:
    print(queue)
    node = queue.popleft()
    if node == K: # 동생 위치에 도달하는 경우
        print(dist[node])
        break
    for next_node in (node-1, node+1, 2*node):
        if visited[next_node] != 1 and next_node <= 100000:
            queue.append(next_node)
            visited[next_node] = 1
            dist[next_node] = dist[node] + 1 # 시간 초 갱신