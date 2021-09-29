def solution(strings,n):

    answer = []     #정리된 답이 들어갈 리스트
    strings.sort()  #주어진 문자열리스트를 우선 정렬
    a= list(map(lambda x:x[n],(strings)))   #람다함수를 사용하여, n자리의 값을 뽑아낸 리스트 a 생성
    a.sort()    #리스트 a를 정렬
    rule = len(strings)     #조건문에서 strings의 인덱스를 삭제하니, 반복문의 반복횟수가 제한되어 만든 것.

    i = 0   #정렬된 단일단어 인덱스 넘버
    j = 0   #strings 의 문자열 인덱스

    while i < rule :
        if a[i] == strings[j][n]:
            answer.append(strings[j])
            strings.remove(strings[j])  #삭제해주는 이유는 n이 같은 문자열을 만나면 그것이 그대로 출력되는 경우가 있어서, 한번 출력하면 삭제되게함.

            i += 1  #같은 n을 만났기 때문에 a리스트에 있는 다음 문자로 넘어가고
            j = 0   # 다른 n을 만났을 때 strings 에서 다음으로 넘겨주는 j가, n을 만나도 그대로 있지않게 하기위해서 즉 처음부터 다시 찾게 해줌!

        elif a[i] != strings[j][n]:

            j += 1  # 다른 n을 만났을 때, strings 내에서 다음 문자열로 넘기게 해줌



    return(answer)

print(solution(['cdx','dha','abd'],2))
print(solution(["abce", "abcd", "cdx"],2))
print(solution(["ccd","ccb","acb"],1))
