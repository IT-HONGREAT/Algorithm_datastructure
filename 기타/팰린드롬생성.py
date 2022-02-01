"""
입력으로 주어진 문자열이 팰린드롬인지 판별한 뒤, 팰린드롬이면 빈 문자열을 출력한다.

입력된 문자열이 팰린드롬이 아닐 경우 문자열을 반으로 나누어 앞부분의 단어를 기준으로 팰린드롬 단어로 만드는 함수를 작성
"""


def solution(s):

    reversed_s = s[::-1]

    if s == reversed_s:
        return ''

    half = len(s)//2
    front_half = s[:half]
    back_half = front_half[::-1]

    return front_half+back_half

s = 'abcdcba'
print(solution(s))

s = 'bannana'
print(solution(s))

s = 'wabe'
print(solution(s))


