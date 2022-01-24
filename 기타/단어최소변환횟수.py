beginWord_1 = "hit"
endWord_1 = "cog"
wordList_1 = ["hot", "dot", "dog", "lot", "log", "cog"]
"""
출력: 5

설명: 가장 짧은 변환 방법은 "hit" -> "hot" -> "dot" -> "dog" -> "cog"이다.
"""

beginWord_2 = "hit"
endWord_2 = "cog"
wordList_2 = ["hot", "dot", "dog", "lot", "log"]

global answer


def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin]
    while stacks:
        # print('stacks',stacks)
        stack = stacks.pop()
        # print('stacks', stacks)
        if stack == target:
            return answer

        for i in range(len(words)):
            # print([j for j in range(len(words[i]))],words[i],stack)
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:

                if visit[i] != 0:
                    continue
                visit[i] = 1
                # print('visit',visit)
                stacks.append(words[i])
        answer += 1
    return answer


def solution(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words]
    answer = dfs(begin, target, words, visit)
    return answer


print(solution(beginWord_1, endWord_1, wordList_1))
print(solution(beginWord_2, endWord_2, wordList_2))
