def solution(gems):
    kind_gem = len(set(gems))
    length_gem = len(gems)

    answer = []

    record_gems = {gems[0]: 1}
    start, end = 0, 0
    while start < length_gem and end < length_gem:
        if len(record_gems) < kind_gem:
            end += 1
            if end == length_gem:
                break
            record_gems[gems[end]] = record_gems.get(gems[end], 0) + 1
        else:
            answer.append((end-start,[start + 1, end + 1]))
            record_gems[gems[start]] -= 1
            if record_gems[gems[start]] == 0:
                del record_gems[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    # print(answer)
    return answer[0][1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))

gems = ["XYZ", "XYZ", "XYZ"]
print(solution(gems))

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
