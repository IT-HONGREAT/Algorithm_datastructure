class LinkedList:
    """더블리 링크드 리스트 구현하기"""

    def __init__(self):
        self.head = None
        self.tail = None

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
