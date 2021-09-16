# 7 3   <3, 6, 2, 7, 5, 1, 4>

from collections import deque
n,k = map(int,input().split())

numbers =[x for x in range(1,n+1)]

answer = []
roopnum = k-1
while len(numbers):
    
    if roopnum >= len(numbers):
        roopnum = roopnum - len(numbers)
    else:
        answer.append(numbers.pop(roopnum))
        roopnum += (k-1)
print("<", ", ".join(str(i) for i in answer), ">", sep='')


