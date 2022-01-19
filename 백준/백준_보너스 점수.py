import sys

sys.stdin = open('input값 파일.txt', 'r')

n = int(input())
record = input()

basic, bonus, total = 0, 0, 0

for i in range(1, n + 1):

    if record[i - 1] == 'O':
        basic += i
        total += bonus
        bonus += 1
    else:
        bonus = 0
print(basic + total)
