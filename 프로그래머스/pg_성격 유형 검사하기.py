def solution(survey, choices):

    points = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i, j in zip(survey, choices):
        if j > 4:
            points[i[-1]] += 1
        elif j < 4:
            points[i[0]] += 1

    answer = ""
    if points["R"] >= points["T"]:
        answer += "R"

    if points["R"] < points["T"]:
        answer += "T"

    if points["C"] >= points["F"]:
        answer += "C"

    if points["C"] < points["F"]:
        answer += "F"

    if points["J"] >= points["M"]:
        answer += "J"

    if points["J"] < points["M"]:
        answer += "M"

    if points["N"] > points["A"]:
        answer += "N"

    if points["N"] <= points["A"]:
        answer += "A"

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
"""
지표 번호	성격 유형
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)
"""
# 기댓값 〉	"TCMA"
