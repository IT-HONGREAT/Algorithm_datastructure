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

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        data = node_to_delete.data
        # 삭제하고 싶은 노드를 node_to_delete 로 받는다
        #1. 지우려는 노드가 링크드 리스트에 마지막 남은 노드
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None

            #노드의 연결이 끊겼으므로 지워진것이나 마찬가지.
        #2. 지우려는 노드가 헤드노드인데, 마지막 남은 경우는 아닐 때
        elif node_to_delete is self.head:
            #헤드를 헤드 다음 노드로 바꿔주고, 새로운 헤드의 전 노드를 None으로 바꿔줌
            self.head = self.head.next
            self.head.prev = None

        #3. 지우려는 노드가 테일노드인데, 마지막 남은 경우는 아닐 때
        elif node_to_delete is self.tail:
            #테일을 테일 전 노드로 바꿔주고, 새로운 테일의 다음 노드를 Nonde으로 바꿔줌!
            self.tail = self.tail.prev
            self.tail.next = None

        #4. 지우려는 노드가 노드들의 사이에 있을 때
        else:
            #지우려는 노드의 다음노드가 , 지우려는 노드 전 노드의 다음 노드를 가르키게 하고
            node_to_delete.prev.next = node_to_delete.next
            #지우려는 노드의 전 노드가, 지우려는 노드 다음노드의 전 노드를 가르키게 한다.
            node_to_delete.next.prev = node_to_delete.prev

        return data


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


# my_list = LinkedList()
#
# my_list.append(1)
# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.append(9)
#
# print(my_list)
#
# tail_node = my_list.tail  # tail 노드
# my_list.insert_after(tail_node, 6)  # tail 노드 뒤에 노드 추가
# print(my_list)
# print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력
#
# # 링크드 리스트 중간에 데이터 삽입
# node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
# my_list.insert_after(node_at_index_3, 3)
# print(my_list)
#
# # 링크드 리스트 중간에 데이터 삽입
# node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
# my_list.insert_after(node_at_index_2, 2)
# print(my_list)


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

# 마지막 노드 삭제
last_node = my_list.head
my_list.delete(last_node)
print(my_list)