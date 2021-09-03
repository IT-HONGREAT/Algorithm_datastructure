list_size = 5
class Queue:
    def __init__(self):
        self.array = [None] * list_size
        self.count = 0
        self.f_idx = 0
        self.b_idx = 0
    def push(self, num):
        if self.count == list_size:
          return -1
        self.count +=1
        self.array[self.b_idx] = num
        self.b_idx = (self.b_idx +1) % list_size
    def pop(self):
        if self.count == 0:
          return -1
        temp = self.array[self.f_idx % list_size]
        self.array[self.f_idx % list_size] = None
        self.f_idx = (self.f_idx +1) % list_size
        self.count -= 1  
        return temp