

def solution(s):
    checker  = 0
    for letter in s:
        if checker < 0:
            return False
        if "(" == letter:
            checker += 1
        if ")" == letter:
            checker -= 1
    return not bool(checker)


if __name__ == '__main__':
    print("테스트 시작")
    print(solution("()()") == True)
    print(solution("(())()") == True)
    print(solution(")()(") == False)
    print(solution("(()(") == False)
    print("테스트 종료")
