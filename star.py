a, b = map(int,input().split())

dis = b-1-a  #마지막 목적지에서 그 전까지 1칸 이동 이기 때문에 사전 설정.
count = 1 #마지막 안전이동 고려.

turn_point = int(dis**0.5)
center_jud = turn_point ** 2

if center_jud < dis < center_jud + turn_point:
    count += turn_point * 2

elif dis == center_jud:
    count += ((turn_point * 2)-1)

print(count)