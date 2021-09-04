# scoville	            K	return
# [1, 2, 3, 9, 10, 12]	7	2


def solution(scoville, K):

    reverse_list = sorted(scoville,reverse=True)

    answer = 0

    while  reverse_list[-1] < K:
        root_node, end_node = 0, len(reverse_list) - 1
        # print('node',root_node, end_node)
        if len(reverse_list) > 1:

            scoed = reverse_list[end_node] + (reverse_list[end_node - 1] * 2)

            reverse_list[end_node] = scoed
            reverse_list.pop(end_node-1)

            # print(reverse_list,100)

            if reverse_list[-1] > reverse_list[-2]:
                reverse_list[-1],reverse_list[-2] = reverse_list[-2],reverse_list[-1]

        else:
            return reverse_list
        answer += 1
    return answer


print(solution([1, 2, 3, 9, 10, 12],7))

