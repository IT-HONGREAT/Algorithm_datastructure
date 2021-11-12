# [1, 1, 1, 1, 1]	3	5
def solution(numbers, target):


    cnt = 0

    for i in range(len(numbers)):
        j = 0
        record = []
        print(record)
        while j < len(numbers):
            record.append(numbers[j])
            j += 1
            if sum(record) != target:
                print(record)
                record.pop(j)
                record.append(-numbers[j])
    



print(solution([1, 1, 1, 1, 1],	3))