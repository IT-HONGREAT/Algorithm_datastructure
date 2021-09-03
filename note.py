# ["abab","bbaa","bababa","bbbabababbbaa"]


def check(ab):
    a = "a"
    b = "b"
    #양끝 a삭제
    while ab[0]==a or ab[-1]==a:
        if ab[0]==a:
            ab = ab[1:]
        if ab[-1]==a:
            ab = ab[:-2]

    #종단 b개수 체크
    c = 0
    while True:
        try:
            ab[c] == b
            c += 1
        except :
            return False
    # print(c)

    #a개수와 종단 b개수 같은지 확인

    if ab.count(a) != c:
        return False
    else:
        return True
    # return True
print(check("bbbabababbbaa"))

def solution(a):

    answer = []

    for i in a:
        if check(i):
            answer.append("True")
        else:
            answer.append("False")

print(solution(["abab","bbaa","bababa","bbbabababbbaa"]))

