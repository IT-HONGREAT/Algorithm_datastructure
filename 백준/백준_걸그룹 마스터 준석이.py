import sys

sys.stdin = open('input값 파일.txt', 'r')

N, M = map(int, input().split())

girl_groups = dict()

# 그룹정보해싱
for _ in range(N):
    group_name = input()
    group_member = []
    member_count = int(input())
    for member in range(member_count):
        group_member.append(input())
    group_member.sort()
    girl_groups[group_name] = group_member

for _ in range(M):
    group_or_member = input()
    one_zero = int(input())
    if one_zero == 1:
        for key, value in girl_groups.items():
            if group_or_member in value:
                print(key)
    else:
        for member in girl_groups.get(group_or_member):
            print(member)
