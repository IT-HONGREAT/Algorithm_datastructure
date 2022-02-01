"""
words	                                                queries                                        	result
["frodo", "front", "frost", "frozen", "frame", "kakao"]	["fro??", "????o", "fr???", "fro???", "pro?"]	[3, 2, 4, 1, 0]
"""

def solution(words, queries):
    answer = []

    # 길이 같고, 해당위치 같기
    # 접미사 / 접두사

    for idx in range(len(queries)):
        length_q = len(queries[idx])
        count = 0

        for word in words:

            if length_q == len(word):

                diff_check = True
                for j in range(len(word)):

                    # print('queries[idx][j]',queries[idx][j])
                    # 접두사
                    if (queries[idx][j] == word[j] or queries[idx][j] == '?') and diff_check:
                        diff_check = True
                    else:
                        diff_check = False
                if diff_check:
                    count += 1
                # print(queries[idx], word, count)
        answer.append(count)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

