class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

# # 기본 노드 생성
# head_node = Node(1)
# node_1 = Node(3)
# node_2 = Node(5)
# node_3 = Node(7)
# node_4 = Node(9)
# tail_node = Node(11)
#
# #next노드연결
#
# head_node.next = node_1
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = tail_node
#
# #기본 링크드 리스트 출력
# iterator = head_node



# while iterator is not None:
#     print("데이터출력 : ",iterator.data)
#     print("다음데이터 : ",iterator.next)
#     iterator = iterator.next

print("====="*20)

# 링크드리스트 클래스 생성(단순히 노드추가 함수만 구현. -> 노드 찾는 함수 추가)
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.index = None

    def insert_after(self, previous_node, data):
        """ 링크드 리스트에서 노드 사이에 새로운 노드 추가"""
        new_node = Node(data)

        #맨 뒤에 삽입 될 때
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        #노드 사이에 삽입 될 때
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node

    def find_node_at(self,index):
        #파라미터 인덱스의 위치에 있는 노드 출력
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""

        iterator = self.head

        while iterator is not None:

            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        if self.head is None:  # 리스트에 아무것도 없는 경우이다.
            self.head = new_node
            self.tail = self.head
        elif self.head is not None:  # 리스트에 뭐라도 있는경우는 헤드를 한칸뒤로 미뤄주면 된다.
            new_node.next = self.head
            self.head = new_node


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
        iterator = self.head

        while iterator is not None:
            res_str += f'{iterator.data} |'
            iterator = iterator.next

        return res_str



#
# new_list = LinkedList()
#
# new_list.append(2)
# new_list.append(4)
# new_list.append(6)
# new_list.append(8)
# new_list.append(10)
# print("문자열로 출력된 링크드 리스트 : " , new_list)
#
# print("원하는 노드의 인덱스 값을 넣으면 노드값이 출력 : ", new_list.find_node_at(3).data)
# print("====="*20)
#
# linked_list = LinkedList()
#
# # 여러 데이터를 링크드 리스트 마지막에 추가
# linked_list.append(3)
# linked_list.append(6)
# linked_list.append(9)
# linked_list.append(12)
# linked_list.append(15)
#
# node_with_11 = linked_list.find_node_with_data(11)
#
# if not node_with_11 is None:
#     print(node_with_11.data)
# else:
#     print("11를 갖는 노드는 없습니다")

print("====="*20)
#insert 테스트위한 새로운 링크드 리스트 생성

my_list = LinkedList()

#노드 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)


print("my_list : ",my_list)

node_2 = my_list.find_node_at(2)
print("node_2 : ", node_2.data)

my_list.insert_after(node_2,6)
print(my_list)

node_4 = my_list.find_node_at(4)
print("node_4 : ", node_4.data)

my_list.insert_after(node_4,10)
print(my_list)

print("====="*20)

linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(7)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

print(linked_list)