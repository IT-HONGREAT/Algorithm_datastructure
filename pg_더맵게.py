# scoville	            K	return
# [1, 2, 3, 9, 10, 12]	7	2

import heapq
def solution(scoville, K):


    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:

        if len(scoville) >  1:
            # print('1',scoville)
            answer += 1

            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            sconum = first + (second * 2)
            heapq.heappush(scoville,sconum)
            # print('2',scoville)

        else:
            return -1
    return answer


print(solution([1, 2, 3, 9, 10, 12],7))

