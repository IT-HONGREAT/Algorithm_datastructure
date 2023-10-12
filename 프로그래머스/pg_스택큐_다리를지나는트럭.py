from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = 0  # 다리 위의 트럭 무게 합을 저장하는 변수

    truck_weights = deque(truck_weights)

    while bridge:
        answer += 1
        bridge_weight -= bridge.popleft()  # 다리에서 트럭이 내려갈 때 무게 감소

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck  # 다리에 트럭이 올라갈 때 무게 증가
            else:
                bridge.append(0)
        else:
            if bridge_weight == 0:
                break

    return answer


if __name__ == "__main__":
    print("CASE1 : ", solution(2, 10, [7, 4, 5, 6]) == 8)
    print("CASE2 : ", solution(100, 100, [10]) == 101)
    print("CASE3 : ", solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)
