
# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5
def solution(priorities, location):
    max_num = max(priorities)
    max_loc = priorities.index(max(priorities))
    information = [(n, i) for i, n in enumerate(priorities)]

    newlist = information[max_loc:] + information[:max_loc]
    founder = max_num

    count = 1
    while founder > 0:

        if newlist[0][0] == founder:

            newlist.pop(0)
            check = newlist.pop(0)
            if check[1] == location:

                return count
        print(newlist)

        founder -= 1
        count += 1

    # return information



print(solution([2,1,3,2],2))
# print(solution([1, 1, 9, 1, 1, 1],0))


