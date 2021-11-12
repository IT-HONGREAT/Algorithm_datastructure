# 4 4
# 3 0 1 4

H,W = map(int,input().split())

w_axis = list(map(int,input().split()))

def twopointer(height):
    if not height:
        return 0

    volume = 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max,right_max = max(height[left], left_max) , max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1

        else:
            volume += right_max - height[right]
            right -= 1

    return volume


print(twopointer(w_axis))