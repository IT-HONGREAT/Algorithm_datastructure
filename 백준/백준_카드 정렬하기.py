# 3
# 10
# 20
# 40
import heapq
n = int(input())
heap = []

for _ in range(n):
    number = int(input())
    heapq.heappush(heap,number)

answer = 0
while len(heap) >= 2:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    temp = one + two
    answer += temp
    heapq.heappush(heap,temp)

print(answer)

