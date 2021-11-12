# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# 2	[2,1,1,0]
# ["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]
# 3	[0,0]
# 메일; 정지당했을때(k도달했을때)
from collections import Counter
def solution(id_list, report, k):
    report = set(report)

    count_dict = {}
    for i in id_list:
        count_dict[i] = 0

    #신고당한 사람 저장
    warned = []
    for names in report:
        a,b = names.split()
        warned.append(b)

    #k번 이상 신고당한 사람 목록
    stopped_id = []
    # print(Counter(warned).values())
    for c in Counter(warned):
        if Counter(warned)[c] >= k:
            stopped_id.append(c)
    # print("d",stopped_id)

    for find in report:
        a, b = find.split()
        if b in stopped_id:
            count_dict[a] += 1


    return list(count_dict.values())

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))