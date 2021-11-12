def solution(s):
    if ('p' not in s )and ('y' not in s):
        return True

    s1 = s.lower()
    if (s1.count('p') == s1.count('y')):
        return True



    else:
        return False



print(solution("pPoooyY"))
print(solution('jijijijy'))
