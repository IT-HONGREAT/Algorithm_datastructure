# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
#
# n = int(input())
# num = {}
# ns = list(map(int,input().split(" ")))
# for i in ns:
#     num[i] = 1
#
# m = int(input())
#
# ms = list(map(int,input().split(" ")))
#
# for j in ms:
#     if j in num.keys():
#         print(num[j])
#     else:
#         print(0)

#set풀이

n = int(input())
array = set(map(int,input().split()))
m = int(input())
x  = list(map(int,input().split()))

for i in x:
    if i not in array:
        print("0")
    else:
        print("1")