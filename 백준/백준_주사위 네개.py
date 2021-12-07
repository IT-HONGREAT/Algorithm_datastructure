# 같은 눈이 4개가 나오면 50,000원+(같은 눈)×5,000원의 상금을 받게 된다.
# 같은 눈이 3개만 나오면 10,000원+(3개가 나온 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개씩 두 쌍이 나오는 경우에는 2,000원+(2개가 나온 눈)×500원+(또 다른 2개가 나온 눈)×500원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.


def money():
    array = sorted(list(map(int,input().split())))

    if len(set(array)) == 1:
        return 50000 + array[0] * 5000

    if len(set(array)) == 2:
        if array[1] == array[2]:
            return 10000 + array[1] * 1000

        else:
            return 2000 + array[0] * 500 + array[-1] * 500

    for i in range(3):
        if array[i] == array[i+1]:
            return 1000 + array[i]*100


    return array[-1]*100



n = int(input())

print(max(money() for i in range(n)))