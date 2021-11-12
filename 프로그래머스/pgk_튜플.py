# "{{4,2,3},{3},{2,3,4,1},{2,3}}"  -> [3, 2, 4, 1]

def solution(s):
    numbers = []
    listing = s.replace("},{",'.').replace("{{","").replace("}}","")
    seper = sorted(listing.split("."),key=len)

    for i in range(len(seper)):
        # print(seper[i])
        numbers.append(seper[i])
    # print(numbers)
    #number 정렬기준 선입선
    answer = []
    for j in numbers:
        a = (j.split(","))
        # print(a)

        for k in a:
            # print(k)
            if k not in answer:
                answer.append(k)

    return [int(x) for x in answer]

    #     if j not in answer:
    #         answer.append(j)
        # for k in j:
        #     if k not in answer:
        #         answer += k
    # print(answer)
    # realan = [int(x) for x in answer]
    # return realan


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

print(solution("{{20,111},{111}}"))