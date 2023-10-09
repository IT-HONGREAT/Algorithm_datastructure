
def judge_popping(number:int) -> bool:
    if number >= 100:
        return True
    return False


def solution(progresses, speeds):
    answer = []

    while progresses:
        # 각 작업에 대한 진도율 업데이트
        progresses = [p + s for p, s in zip(progresses, speeds)]
        deploy_count = 0
        # 앞에서부터 진도율이 100%인 작업이 몇 개인지 확인
        while progresses and judge_popping(progresses[0]):
            deploy_count += 1
            progresses.pop(0)
            speeds.pop(0)

        if deploy_count:
            answer.append(deploy_count)

    return answer


if __name__ == '__main__':
    print(solution([93, 30, 55],[1, 30, 5]) == [2, 1])
    print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])==[1, 3, 2])
