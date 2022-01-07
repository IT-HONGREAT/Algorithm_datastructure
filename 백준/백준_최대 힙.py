import heapq
import sys

n = int(sys.stdin.readline())

heap = []

count_zero = 0
push_count  = 0
for i in range(n):
    num = int(sys.stdin.readline())



    if num == 0:
        count_zero += 1

    if num != 0:
        heapq.heappush(heap, (-num, num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
        push_count += 1
# if count_zero != push_count:
#     print(0)

# print(count_zero)
# print(push_count)
# for num in nums:
#   heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

# print(heapq.heappop(heap)[1])
# print(heapq.heappop(heap)[1])  # index 1
# print(heapq.heappop(heap)[1])  # index 1
# print(heapq.heappop(heap)[1])  # index 1

