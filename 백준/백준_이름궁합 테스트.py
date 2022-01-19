import sys

sys.stdin = open('input값 파일.txt', 'r')
# input
# 8 14
# LEESIYUN MIYAWAKISAKURA

"""문제에서 필요한 획수를 일일히 쓰기귀찮아서 복붙하고 딕셔너리로 저장"""
alpha = "A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z"
number = "3	2	1	2	4	3	1	3	1	1	3	1	3	2	1	2	2	2	1	2	1	1	1	2	2	1"

alpha_number = dict()
for key, value in zip(alpha.split(), number.split()):
    alpha_number[key] = value




N, M = map(int, input().split())
name_1, name_2 = map(str,input().split())


"""이름궁합로직"""
def percent(numbers: str) -> str: #전부 이어진 숫자 받기
    while True:
        summing = ""
        for i in range(len(numbers)-1):
            if not numbers[i]:
                continue
            # print('i,i+1',i,i+1)
            summing += str((int(numbers[i]) + int(numbers[i + 1])) % 10)
            # print(summing,int(numbers[i]) + int(numbers[i + 1]))
        numbers = summing
        # print('numbers',numbers)
        if len(numbers) == 2:
            if int(numbers)<10:
                return numbers[1]+'%'
            return numbers+'%'   #퍼센트출력


#문자를 획수화
new_1,new_2 = '',''
for i in name_1 : new_1 += alpha_number[i]
for i in name_2 : new_2 += alpha_number[i]

#획수화 된 문자 길이판단후 더 긴 문자열 뒷부분 남은글자 추가하기

number = ''
for i in zip(new_1, new_2):
    number += i[0] + i[1]

if N>M:
    number += new_1[M:]

elif N < M:
    number += new_2[N:]

print(percent(number))
