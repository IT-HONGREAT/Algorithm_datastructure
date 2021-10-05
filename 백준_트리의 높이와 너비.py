# 19
# 1 2 3
# 2 4 5
# 3 6 7
# 4 8 -1
# 5 9 10
# 6 11 12
# 7 13 -1
# 8 -1 -1
# 9 14 15
# 10 -1 -1
# 11 16 -1
# 12 -1 -1
# 13 17 -1
# 14 -1 -1
# 15 18 -1
# 16 -1 -1
# 17 -1 19
# 18 -1 -1
# 19 -1 -1


class Node:

    def __init__(self, data, left_node, right_node):
        self.parent = -1
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def in_order(node, level):   #중위순회로 탐색하면 왼쪽부터 봤을 때 일직선 상에서 순차적으로 표현되기 때문에 중위순회를 사용한다.
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)

    level_min[level] = min(level_min[level], x) #가장 작은 값을 반복적으로 찾음
    level_max[level] = max(level_max[level], x) #가장 큰 값을 반복적으로 찾음
    x += 1

    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1

for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

# 트리 입력
for _ in range(n):
    data, left_node, right_node = map(int, input().split())
    tree[data].left_node = left_node
    tree[data].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = data       #왼쪽노드 방문 후 부모값으로 설정
    if right_node != -1:
        tree[right_node].parent = data      #오른쪽노드 방문 후 부모값으로 설정

for i in range(1, n + 1):   #부모가 없는 노드가 루트노드
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1

for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)


