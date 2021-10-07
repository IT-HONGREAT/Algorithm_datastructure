# 4 2
# 4 2
# 3 1
#

import heapq

n, m = map(int,input().split())

array = [[] for i in range(n + 1)]  #2차원 배열에서의 각 인덱스를 x정보라고 생각한다.
indegree = [0] * (n + 1)  #간선으로 이어진 노드 y가 몇번이나 간선으로 연결되어있는지 세준다.

heap = []
result = []
for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

print('array : ',array)
print('indegree : ',indegree)

for i in range(1, n + 1):
    if indegree[i] == 0:   #진입 차수가 0 인 노드를 인식하고
        heapq.heappush(heap,i)  #어떤 것인지 힙에 넣는다.

print('heap : ', heap)
while heap:     #큐와 같은 역할이다.
    data = heapq.heappop(heap)     #가장 작은 숫자를 우선으로 뽑아서
    result.append(data)            #정답 리스트에 넣는다
    for y in array[data]:           #2차원 배열에서 각 인덱스 [] 를 돌아서 탐색한다.
        indegree[y] -= 1            #위상정렬그래프에서 간선을 하나씩 삭제해준다.
        if indegree[y] == 0:        #시작노드는 상속된 간선이 없고(진입차수가 0)
            heapq.heappush(heap, y)  #이 진입 차수가 0이 된 정점을 큐에 삽입한다.
print('heap2 : ', heap)
print('result : ', result)

for i in result:
    print(i, end=' ')