#11004번

# 3
# 7


n,k = map(int,input().split())

array = list(map(int,input().split()))

array.sort()
print(array[k-1])