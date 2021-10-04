# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# ---------
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

# 클래스로 트리구조 틀 만들기

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

#전위순회 함수

def pre_order(node):  # 재귀로 구현한다.
    print(node.data,end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data,end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data,end='')


n = int(input())
tree = {}

for _ in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node) # 트리의 각 데이터의 노드에 대한 정보를 담아둔다.(자신,왼쪽자식,오른쪽자식)



pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])