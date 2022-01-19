import sys
sys.stdin = open('input값 파일.txt','r')
# input
# 5
# 27 35 92 75 42

n = int(input())

numbers = list(map(int,input().split()))
print(max(numbers)-min(numbers))


