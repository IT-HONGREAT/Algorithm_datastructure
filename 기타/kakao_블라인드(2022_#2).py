# '437674',3
# '110011',10
# 437674을 3진수
import re


def solution(n, k):
    new = ''

    while n > 0:
        n, mod = divmod(n, k)
        new += str(mod)

    new_num =  str(new[::-1])
    strings = new_num

    # p = re.compile('^0\S0$').search(strings)
    p = re.split('^0\w|0\w0|0*0|\w0$',strings)
    # for i in strings:
    #
    #     m = p.search(i)
    #
    #     if m:
    #         print(m.group(0))

    return len(p)

print('211020101011'.split('0'))
print(solution(437674,3))
print(solution(110011,10))