class Node:

    def __init__(self,data):

        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """더블리 링크드 리스트 구현하기"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        """새로운 노드 추가"""
        new_node = Node(data)

        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 리스트가 비어있지 않은 경우
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self,data):
        """제일 앞에 노드 추가"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node



    def insert_after(self,previous_node,data):
        """새로운 노드 삽입연산"""

        new_node = Node(data)

        # 맨뒤에 삽입 하는 경우
        if previous_node is self.tail:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
            #새로운 노드를 원래의 링크드리스트에 연결한다.

            #새로운 노드를 링크드리스트에 연결
            new_node.prev = previous_node
            new_node.next = previous_node.next

            #원래 있던 노드에 새로운 노드 연결
            previous_node.next.prev = new_node
            previous_node.next = new_node



    def find_node_at(self,index):

        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self,data):

        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):

        res_str = "|"

        iterator = self.head

        while iterator is not None:

            res_str += " {} |".format(iterator.data)
            iterator = iterator.next

        return res_str


my_list = LinkedList()

my_list.append(1)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(9)

print(my_list)

tail_node = my_list.tail  # tail 노드
my_list.insert_after(tail_node, 6)  # tail 노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)