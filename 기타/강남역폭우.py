def trapping_rain(buildings):

    top_height = max(buildings)
    top_index = 0
    for i in range(len(buildings)):
        if buildings[i] == top_height:
            top_index = i


    start_l_index = 0
    for i in range(top_index):
        if start_l_index == 0 and buildings[i] != 0:
            start_l_index = i
            break
    wall_l = 0 #벽높이
    water_l = 0
    for i in range(start_l_index,top_index):
        if wall_l < buildings[i]:
            wall_l = buildings[i]

        water = wall_l - buildings[i]
        water_l += water

    start_r_index = len(buildings)-1
    for i in range(len(buildings)-1,top_index,-1):
        if start_r_index == len(buildings)-1 and buildings[i] != 0:
            start_r_index = i
            break
    wall_r = 0  # 벽높이
    water_r = 0
    for i in range(len(buildings)-1, top_index,-1):
        if wall_r < buildings[i]:
            wall_r = buildings[i]

        water = wall_r - buildings[i]
        water_r += water

    # print("l",water_l)
    # print("r",water_r)
    return water_l+water_r
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))