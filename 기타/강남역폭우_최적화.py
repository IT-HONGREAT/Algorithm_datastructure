def trapping_rain(buildings):
    total_height = 0

    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치 판단
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        #좌우 높이 보고 낮은 것 판단하고 그 높이가 빗물이 담길 수 있는 높이임
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        if upper_bound - buildings[i] > 0:
            total_height += upper_bound - buildings[i]
        # total_height += max(0, upper_bound - buildings[i])

    return total_height

# 테스트
print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))