# def pop_first_item(my_dict):
#     """
#     dict일때 사용할 함수. 튜플로 변환하면서 필요가 없어졌지만, 기억해두자.
#     :param my_dict:
#     :return:
#     """
#     first_key = next(iter(my_dict))
#     return my_dict.pop(first_key)


def find_bigger(dict_value: list, measurable_num: int) -> bool:
    """비교하는 함수"""
    for other in dict_value:
        if measurable_num < other[1]:
            return True
    return False


def solution(priorities, location):
    answer = 0
    # 인덱스 넘버 기록
    idx_number = [(idx, number) for idx, number in enumerate(priorities)]

    # 큐 구현
    while idx_number:
        first_obj: tuple = idx_number.pop(0)
        if not find_bigger(idx_number, first_obj[1]):
            answer += 1
            if location == first_obj[0]:
                return answer
            continue
        idx_number.append(first_obj)

    return answer


if __name__ == "__main__":
    """
    answer이 몇번째로 실행되는것인지 알려줌.
    location 은 인덱스넘버
    """
    print("case1 : ", solution([2, 1, 3, 2], 2) == 1)
    print("case2 : ", solution([1, 1, 9, 1, 1, 1], 0) == 5)
