import itertools
from itertools import cycle


def solution(a, b):

    day = cycle('FRI,SAT,SUN,MON,TUE,WED,THU'.split(','))

    year = {}
    # a 는 월, b 는 일(1,3,5,7,8,10,12 - 31/4,6,9,11 - 30 / 2 - 29
    m = 1
    d = 1

    yo = itertools.cycle(day)  # cycle로 요일을 변수로 뽑아줌

    while m < 13:
        i = next(yo)
        year['{}_{}'.format(m, d)] = i
        d += 1
        if d == 32:
            m += 1
            d = 1
        elif m == 2 and d == 30:
            m += 1
            d = 1
        elif (m == 4 or m == 6 or m == 9 or m == 11) and d >= 31:
            m += 1
            d = 1
    # print(year)
    return year['{}_{}'.format(a, b)]


print(solution(1,1))
print(solution(5,24))