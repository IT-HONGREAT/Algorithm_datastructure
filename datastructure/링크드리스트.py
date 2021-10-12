class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

# 기본 노드 생성
head_node = Node(1)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
node_4 = Node(9)
tail_node = Node(11)

#next노드연결

head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = tail_node

#기본 링크드 리스트 출력
iterator = head_node

while iterator is not None:
    print("데이터출력 : ",iterator.data)
    print("다음데이터 : ",iterator.next)
    iterator = iterator.next


# 링크드리스트 클래스 생성(단순히 노드추가 함수만 구현.)
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):  #링크드리스트에 데이터를 넣어주자.
        #새로운 노드 설정
        new_node = Node(data)

        #두가지 경우가 있을 것이다.. 링크드리스트가 비어있거나, 이미 데이터가있거나!
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    #링크드리스트를 문자열로 정리
    def __str__(self):
        res_str = "|"
        iterator3 = self.head

        while iterator3 is not None:
            res_str += f'{iterator3.data} |'
            iterator3 = iterator3.next

        return res_str




new_list = LinkedList()

new_list.append(2)
new_list.append(4)
new_list.append(6)
new_list.append(8)
new_list.append(10)
print("문자열로 출력된 링크드 리스트 : " , new_list)

# iterator2 = new_list.head
#
# while iterator2 is not None:
#     print("링크드리스트 추가 후 출력 : " ,iterator2.data)
#     print("다음데이터 : ",iterator2.next)
#     iterator2 = iterator2.next
