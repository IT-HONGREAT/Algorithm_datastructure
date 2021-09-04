print("heap 구현")

class Heap:
    def __init__(self, data):
        self.heap_list = list()
        self.heap_list.append(None)
        self.heap_list.append(data)

    def move_down(self,popped_idx):
        left_child_popped_idx = popped_idx * 2  #삭제한 노드의 자식노드 중 왼쪽
        right_child_popped_idx = popped_idx * 2 + 1 # 삭제한 노드의 자식노드 중 오른쪽

        #3가지 경우의 수를 염두해야 한다. 왼쪽자식노드가 없을 때/ 오른쪽 자식노드만 없을 때/ 자식노드(왼쪽, 오른쪽)이 전부 있을 때/

        #왼쪽 자식노드가 없을 때: 삭제된 노드의 자식노드의 인덱스 번호가 높으니까 그 번호가 힙리스트의 길이 보다 크거나 같다고 하는 경우임
        if left_child_popped_idx >= len(self.heap_list):
            return False  #거짓이므로 pop함수의 반복문 종료
        #오른쪽 자식노드만 없을 때(즉 왼쪽 자식노드는 있다) : 역시 리스트의 길이로 판단한다.
        elif right_child_popped_idx >= len(self.heap_list):
            #힙리스트에서 삭제한 인덱스번호가 왼쪽 자식노드보다 커야함. 작으면 안됨.
            if self.heap_list[popped_idx] < self.heap_list[left_child_popped_idx]:
                return True  #삭제된 부모노드가 왼쪽 자식노드보다 작다는 것이므로 이동할 필요가 있기 때문에 참

            else:
                return
        #자식노드가 왼쪽 오른쪽 전부 있을 경우

        else:
            #왼쪽 노드가 오른쪽 노드보다 크다? 안되는 것임.
            if self.heap_list[left_child_popped_idx] > self.heap_list[right_child_popped_idx]:
                #삭제한 노드가 왼쪽 자식노드보다 작다? 역시 안됨.
                if self.heap_list[popped_idx] < self.heap_list[left_child_popped_idx]:
                    return True #그러므로 참값을 줘서 교체진행
                else:
                    return False
            else:
                #삭제한 노드가 오른쪽 자식노드보다 역시 작으면 안됨!
                if self.heap_list[popped_idx] < self.heap_list[right_child_popped_idx]:
                    return True
                else:
                    return False


    #삭제 추가
    def pop(self):

        #힙 리스트가 비어있을 때를 인식
        if len(self.heap_list) <= 1:
            return None

        returned_data = self.heap_list[1]

        #힙 삭제의 원리인 마지막 노드와의 교환
        self.heap_list[1] = self.heap_list[-1]
        #마지막 노드를 최상단에 넣어주고 삭제
        del self.heap_list[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2  # 삭제한 노드의 자식노드 중 왼쪽
            right_child_popped_idx = popped_idx * 2 + 1  # 삭제한 노드의 자식노드 중 오른쪽

            if right_child_popped_idx >= len(self.heap_list):
                # 힙리스트에서 삭제한 인덱스번호가 왼쪽 자식노드보다 커야함.
                if self.heap_list[popped_idx] < self.heap_list[left_child_popped_idx]:
                    #삭제한 노드가 왼쪽 자식노드보다 작기 때문에 교체!!
                    self.heap_list[popped_idx],self.heap_list[left_child_popped_idx] = self.heap_list[left_child_popped_idx],self.heap_list[popped_idx]

                    popped_idx = left_child_popped_idx #삭제된 노드의 인덱스 번호는 왼쪽 자식노드의 인덱스번호와 교체.


                else:
                    #왼쪽 자식노드가 오른쪽 자식노드보다 클 경우
                    if self.heap_list[left_child_popped_idx] > self.heap_list[right_child_popped_idx]:
                        # 삭제된 노드가 왼쪽보다 작으면 안됨! 그렇기 때문에
                        if self.heap_list[popped_idx] < self.heap_list[left_child_popped_idx]:
                            #역시 교체 진행
                            self.heap_list[popped_idx],self.heap_list[left_child_popped_idx] = self.heap_list[left_child_popped_idx],self.heap_list[popped_idx]
                            popped_idx = left_child_popped_idx

                        else:
                            #오른쪽도 비교 후 교체
                            if self.heap_list[popped_idx] < self.heap_list[right_child_popped_idx]:
                                self.heap_list[popped_idx],self.heap_list[right_child_popped_idx] = self.heap_list[right_child_popped_idx],self.heap_list[popped_idx]
                                popped_idx = right_child_popped_idx
        return returned_data


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
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_list)
print(heap.pop())
print(heap.heap_list)