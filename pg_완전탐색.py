def solution(answers):

    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count_one = 0
    count_two = 0
    count_three = 0

    for i in range(0,len(answers)):
        if one[i % 5] == answers[i]:def solution(answers):

    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count_one = 0
    count_two = 0
    count_three = 0

    for i in range(0,len(answers)):
        if one[i % 5] == answers[i]:
            count_one += 1
        if two[i % 8] == answers[i]:
            count_two += 1
        if three[i % 10] == answers[i]:
            count_three += 1

    rank = [0, count_one, count_two, count_three]

    temp = max(rank)
    answer = []
    for i in range(len(rank)):
        if rank[i] == temp:
            answer.append(i)

    return answer
            count_one += 1
        if two[i % 8] == answers[i]:
            count_two += 1
        if three[i % 10] == answers[i]:
            count_three += 1

    rank = [0, count_one, count_two, count_three]

    temp = max(rank) 
    answer = []
    for i in range(len(rank)):
        if rank[i] == temp:
            answer.append(i)

    return answer

print(solution([3,3,3,32,3,4,5,2,1,1,1,1,1,2,3,12,]))