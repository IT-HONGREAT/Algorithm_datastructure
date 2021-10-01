# arr1	        arr2	        return
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


#위의 코드를 보다 파이써닉하게 구현하는 연습
def solution2(arr1, arr2):
    answer = [[ c + d for c, d in zip(a, b)]for a, b in zip(arr1, arr2)]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
print(solution2([[1,2],[2,3]],[[3,4],[5,6]]))