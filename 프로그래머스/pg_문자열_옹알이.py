def solution(babbling):
    answer = 0
    vs = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for v in vs:
            if b.count(v) < 2:
                b = b.replace(v, " ")

        b = b.replace(" ", "")

        if not b:
            answer += 1

    return answer


if __name__ == "__main__":
    """ """
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]) == 1)
    print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaxa"]) == 3)
