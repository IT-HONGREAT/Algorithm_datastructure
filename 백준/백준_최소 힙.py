# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32

import heapq

n = int(input())
heap = [] #힙 기본 리스트 세팅

answer = [] #결과를 담을 값들 출력

for _ in range(n):
    number = int(input())
    if number == 0:
        if heap:  # 힙에 최소한 하나의 자료가 담겨있을 경우이다. len(heap) != 0: 과 같다.
            answer.append(heapq.heappop(heap))
        else:
            answer.append(0)
    else:
        heapq.heappush(heap, number)

for i in answer:
    print(i)
