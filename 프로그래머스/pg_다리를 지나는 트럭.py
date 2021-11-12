# 2	    10	[7,4,5,6]	                    8
# 100	100	[10]	                        101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110

def solution(bridge_length, weight, truck_weights):
    sec = 0
    bridge = [0] * bridge_length

    while len(bridge):
        sec += 1
        # print(bridge)
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return sec
print(solution(2,10,[7,4,5,6]))

