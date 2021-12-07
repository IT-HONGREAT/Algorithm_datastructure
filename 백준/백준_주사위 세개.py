# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

numbers = sorted(list(map(int,input().split())))



if len(set(numbers)) == 1:
    print(10000 + numbers[0]*1000)

elif len(set(numbers)) == 2:
    print(1000 + numbers[1]*100)

elif len(set(numbers)) == 3:
    print(numbers[2]*100)


