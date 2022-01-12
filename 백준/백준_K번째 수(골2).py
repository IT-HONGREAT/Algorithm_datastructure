"""
리스트컴프리헨션으로 배열생성하고 완전탐색 -> 메모리초과
matrix = [ [i*j for i in range(1, n+1)]  for j in range(1, n+1) ]  각 row가 구구단형식으로 되어있음.
"""
# 3
# 7



"""

배열전체를 만드는 것 자체가 메모리를 초과한다.
규칙을 적절히 이용한다.
n=3일때
[[1,2,3],
 [2,4,6],
 [3,6,9]]
 이렇게 되어있는데..

규칙
1 이하의 수는 1개
2 이하의 수는 3개
3 이하의 수는 5개
4 이하의 수는 6개
5 이하의 수는 6개   => 5없음
6 이하의 수는 8개   => 6없음
7 이하의 수는 8개   => 7없음
8 이하의 수는 8개
9 이하의 수는 9개

배열의 x이하 수 - (배열 x이하 수 - 1) == 0 이라면, x는 없음.

"""
n = int(input())
k = int(input())



def k_number(n,start,check):
    answer = 0

    while start <= check:
        mid = (start + check) // 2 # 이진탐색
        count = 0
        for i in range(1, n+1):
            count += min(mid//i,n)

        print('mid',mid,'count',count)
        if count < check:
            start = mid + 1
        else:
            answer = mid
            check = mid -1



    return answer

print('ans',k_number(n, 0, k))
