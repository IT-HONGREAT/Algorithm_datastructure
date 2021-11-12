# 14

#첫번째
n = int(input())

birds = n

sec = 0
number = 0
while birds:
    number += 1
    for _ in range(number):
        if birds:
            birds -= 1
    if number >= birds:
        number = 0

    sec += 1
    # print('birds',birds)
print(sec)

#두번째
n = int(input())

birds = n

sec = 0
number = 0
while birds:
    number += 1
    if birds >= number:
        birds -= number

    else:
        number = 1
        birds -= number

    sec += 1
    # print('birds',birds)
print(sec)


