# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3

def solution(people, limit):

    people.sort()

    start, end,cnt = 0, len(people)-1,len(people)

    while start < end:
        if people[start]+people[end] <= limit:
            cnt-=1
            start +=1
        end-=1
    return  cnt


print(solution( [70, 50, 80, 50],	100))
# print(solution([70, 80, 50],	100	))