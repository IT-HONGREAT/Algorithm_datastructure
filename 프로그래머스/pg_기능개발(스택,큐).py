import math

def solution(progresses, speeds):
    from collections import Counter


    last = []

    for i in range(len(progresses)):
        a = (100 - progresses[i]) / speeds[i]
        last_days = math.ceil(a)
        last.append(last_days)

    for i in range(len(last)):
        for j in range(i + 1, len(last)):
            if last[i] > last[j]:
                last[j] = last[i]

    return list(Counter(last).values())  #not mine

print(solution([93,30,55],[1,30,5]))