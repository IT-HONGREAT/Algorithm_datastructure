# scoville	K	return
# [1, 2, 3, 9, 10, 12]	7	2
# 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
# 가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
#
# 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
# 새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
# 가진 음식의 스코빌 지수 = [13, 9, 10, 12]

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
def makesco(numbers, fir,sec):

    return numbers[fir] + (numbers[sec]*2)


def solution(scoville, K):

    fir = 0
    sec = 1
    # 모든수 스코빌 지수 -1 판단
    count = len(scoville)-1
    #정답은 횟수
    answer = 0

    while scoville[0]<=K:
        scoville.sort()
        new = makesco(scoville,fir,sec)

        print('sco',scoville)
        mixed = [new] + scoville[2:]
        print('m',mixed)
        scoville.pop(sec)
        scoville = mixed
        # print(count)
        count-=1

        if count == 2 or makesco(scoville,-1,-2)<K:
            return -1
        answer +=1
    return answer

print(solution([1, 2, 3, 9, 10, 12]	,7))