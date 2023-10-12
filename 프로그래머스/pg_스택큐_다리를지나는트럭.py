from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    while bridge or truck_weights:
        answer += 1
        one_truck_weight = 0
        bridge.popleft()
        if truck_weights:
            one_truck_weight = truck_weights[0]
        try_weight = sum(bridge) + one_truck_weight
        if try_weight <= weight:
            if truck_weights:
                one_truck = truck_weights.popleft()
                bridge.append(one_truck)
            else:
                continue
        if try_weight > weight:
            bridge.append(0)
    return answer


if __name__ == "__main__":
    print("CASE1 : ", solution(2, 10, [7, 4, 5, 6]) == 8)
    print("CASE2 : ", solution(100, 100, [10]) == 101)
    print("CASE3 : ", solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)
