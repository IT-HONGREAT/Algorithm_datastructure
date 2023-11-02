"""
나이트가 움직일 수 있는 경우의 수
8*8
a1 -> 2
가로 세로
1,a 1,b 1,c
2,a
3,a

"""


loc = str(input())


def trans_coor(origin_data):
    mapper = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
    }

    return mapper[origin_data]


def night_movement(x, y) -> int:
    count = 0
    kinds = [
        [2, -1],
        [2, 1],
        [-2, -1],
        [-2, 1],
        [-1, -2],
        [1, -2],
        [-1, 2],
        [1, 2],
    ]  # "DDR"

    for kind in kinds:
        temp_x, temp_y = x + kind[0], y + kind[1]
        if 0 <= temp_x < 8 and 0 <= temp_y < 8:
            count += 1
    return count


def solution(location) -> int:
    y, x = trans_coor(loc[0]), trans_coor(loc[1])
    return night_movement(x, y)


print(solution(loc))
