# 5 3
# 1
# 2
# 8
# 4
# 9

N, C = map(int,input().split())

house = []

for i in range(N):
    house.append(int(input()))
house = sorted(house)

min_gap = 1  #초기 8
max_gap = house[-1] - house[0] #초기 1
result = 0

while min_gap <= max_gap:
    mid = (min_gap + max_gap) // 2
    value = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= value + mid:
            value = house[i]
            count += 1

    if count >= C:  #설치 가능
        min_gap = mid + 1
        result = mid
    else:  #설치 불가
        max_gap = mid -1


print(result)

