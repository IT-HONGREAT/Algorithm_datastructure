# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841"	4	"775841"



from itertools import combinations

def solution(number, k):

    comb = sorted(["".join(i) for i in combinations(number,len(number)-k)])
    return comb[-1]





print(solution("1924", 2))
print(solution("1231234",3))
print(solution("4177252841"	,4))
