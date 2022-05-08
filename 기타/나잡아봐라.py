"""
코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.

코니의 위치: 11 → 12 → 14 → 17 → 21 → 26
브라운의 위치: 2 → 3 → 6 → 12 → 13 → 26
브라운은 코니를 5초 만에 잡을 수 있다.
"""


def solution(C, B):
    sec = 1
    q = [B]
    result = 0
    while True:
        C += sec

        # 로직
        for _ in range(len(q)):
            Brown = q.pop(0)
            plus_1 = Brown + 1
            minus_1 = Brown - 1
            gob_2 = Brown * 2

            if (plus_1 == C) or (minus_1 == C) or (gob_2 == C):
                result = sec
                return result

            else:
                q.append(plus_1)
                q.append(minus_1)
                q.append(gob_2)
        # print(q)
        sec += 1

    return result


print(solution(11, 2))
