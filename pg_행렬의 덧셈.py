# arr1	        arr2	            return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	    [[3],[4]]	    [[4],[6]]


def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1,arr2):
        array = []
        for k in range(len(i)):
            array.append(i[k]+j[k])
        answer.append(array)
    return answer


print(solution( [[1,2],[2,3]],[[3,4],[5,6]]))