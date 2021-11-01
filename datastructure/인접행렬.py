#인접행렬로 그래프 개념 연습
#그래프구현에 익숙해 지기위해 생각해본 좋은 방법!

#노드 0,1,2,3,4,5 (총 6개 지만 그냥 0~5 라고 지정 한다)
#엣지 ( 입력는 0 - 1,2 에서 1,2 를 받는다고 가정해봄)
# 0 - 1,2
# 1 - 0,3,5
# 2 - 0,5
# 3 - 1,4,5
# 4 - 3,5
# 5 - 1,2,3,4

n = int(input())


def graph(n):
    adjancency_matrix = [[0 for _ in range(6)] for _ in range(6)]
    record = []
    for i in range(n):
        nodes = list(map(int,input().split(',')))

        for j in nodes:
            adjancency_matrix[i][j] = 1


    return adjancency_matrix

print(graph(n))


#input값 자동처리

n = 6
nodes = [[1,2],[0,3,5],[0,5],[1,4,5],[3,5],[1,2,3,4]]

def graph(n):
    adjancency_matrix = [[0 for _ in range(6)] for _ in range(6)]
    record = []
    for i in range(n):
        new_nodes = nodes[i]

        for j in new_nodes:
            adjancency_matrix[i][j] = 1


    return adjancency_matrix

print(graph(n))