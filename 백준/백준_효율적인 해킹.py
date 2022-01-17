# 첫째 줄에, N과 M이 들어온다.
# N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다.
# 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며,
# "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 연결저장
    adj[b].append(a)


def bfs(v):
    # 초기설정
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True

    count = 1  # 간선수 저장

    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1
        # print(i, v, q)
    return count


# 입력받고 bfs하나씩 확인해서 간선수 제일 많은것 출력
answer = []
max_value = 0

for i in range(1, n + 1):
    check = bfs(i)  # 컴퓨터번호로 확인

    if check > max_value:
        answer = [i]
        max_value = check

    elif check == max_value:
        answer.append(i)
        max_value = check
answer.sort()
print(*answer)
