"""
입력: intervals = [[1,3],[2,6],[8,10],[15,18]]
출력: [[1,6],[8,10],[15,18]]
설명: 구간 [1,3]와 [2,6]이 겹치므로, [1,6]으로 병합하였다.
"""
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]


def solution(intervals):
    new = []
    for idx in range(len(intervals)):

        if idx == len(intervals) - 1:
            break

        first, second = intervals[idx], intervals[idx + 1]

        if first[0] < max(first[1], second[0]) < second[1] and first[1] >= second[0]:
            new.append([first[0], second[1]])

        else:
            new.append([second[0], second[1]])

    return new


print(solution(intervals))
print(solution(intervals2))
