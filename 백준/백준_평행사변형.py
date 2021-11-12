# 0 0 0 1 1 0   있음
# 0 0 1 0 47 0  없음 -1

from itertools import combinations
n = list(map(int,input().split()))

def length(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)*0.5

x_a,y_a = n[0],n[1]
x_b,y_b= n[2],n[3]
x_c,y_c= n[4],n[5]

length_record = [length(x_a,x_b,y_a,y_b),length(x_b,x_c,y_b,y_c),length(x_c,x_a,y_c,y_a)]
alleng_record = []
for i in combinations(length_record,2):
    alleng_record.append(2*sum(i))

print(alleng_record)

# print(width_record)

