# 6 8 10
# 25 52 60
# 5 12 13
# 0 0 0

def zik(one,two,three):
    if (one**2)+(two**2) == three**2:
        return True
    else:
        return False

while True:

    number = list(map(int,input().split()))
    number.sort()
    n1,n2,n3 = number[0],number[1],number[2]
    if sum(number) == 0:
        break
    if zik(n1,n2,n3):
        print("right")
    else:
        print("wrong")

