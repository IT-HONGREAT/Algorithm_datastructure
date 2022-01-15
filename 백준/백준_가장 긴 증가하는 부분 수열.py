

# 증가할 때 체크하면됨

# 6
# 10 20 10 30 20 50

n = int(input())
array = list(map(int,input().split()))

check = [1] * n

for i in range(1,n):

    for j in range(i):

        if array[j] < array[i]:


            check[i] = max(check[i],check[j]+1)

print(max(check))

