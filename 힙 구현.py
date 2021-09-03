print("heap 구현")

class Heap:
    def __init__(self, data):
        self.heap_list = list()
        self.heap_list.append(None)
        self.heap_list.append(data)


    def move_up(self, inserted_idx):
        #노드가 상위노드와의 관계를 판단

        if inserted_idx <=1:
            #맨위니까
            return False
        parent_idx = inserted_idx // 2
        if self.heap_list[inserted_idx] >self.heap_list[parent_idx]:
            #바로 바꿔주는 것이 아니라 불린값을 줘서 insert 메소드에서 참값으로 받고 교환함
            return True
        else:
            return False

    def insert(self, data):
        #루트에 아무것도 없을 때??
        if len(self.heap_list) == 0:
            self.heap_list.append(None)
            self.heap_list.append(data)
            return True

        self.heap_list.append(data)

        inserted_idx = len(self.heap_list)-1

        #부모노드와 자식 노드를 바꿔줌. 조건은 move_up메소드가 참이어야함.
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_list[inserted_idx],self.heap_list[parent_idx] = self.heap_list[parent_idx], self.heap_list[inserted_idx]
            inserted_idx = parent_idx


        return True

heap = Heap(15)
heap.insert(1)
heap.insert(3)
heap.insert(5)
heap.insert(23)
heap.insert(24)
heap.insert(2)
heap.heap_list.pop(0)
print(heap.heap_list)

