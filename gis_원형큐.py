# [..., 1,2,3,4, ...]
class Queue:
    def __init__(self, length):
        self.array = [None for _ in range(length + 1)]
        self.f_idx = 0
        self.b_idx = 0

    def push(self, num):
        if self.is_full():
            return -1

        self.array[self.b_idx] = num
        self.b_idx = (self.b_idx + 1) % len(self.array)

    def pop(self):
        if self.is_empty():
            return -1

        self.f_idx = (self.f_idx + 1) % len(self.array)
        last_val = self.array[self.f_idx - 1]
        self.array[self.f_idx - 1] = None
        return last_val

    def size(self):
        return (self.b_idx + len(self.array) - self.f_idx) % len(self.array)

    def empty(self):
        return int(self.is_empty())

    def front(self):
        if self.is_empty():
            return -1

        return self.array[self.f_idx]

    def back(self):
        if self.is_empty():
            return -1

        return self.array[self.b_idx - 1]

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        # return self.size() == len(self.array)
        return (self.b_idx + 1) % len(self.array) == self.f_idx


def run_cmd_with_queue(command, queue_obj):
    cmd_type = command[0]

    if cmd_type == "push":
        _, num = command
        res = queue_obj.push(int(num))

        if res:
            print(res)
    elif cmd_type == "pop":
        print(queue_obj.pop())
    elif cmd_type == "size":
        print(queue_obj.size())
    elif cmd_type == "empty":
        print(queue_obj.empty())
    elif cmd_type == "front":
        print(queue_obj.front())
    elif cmd_type == "back":
        print(queue_obj.back())


n = int(input())
queue_obj = Queue(4)

for _ in range(n):
    run_cmd_with_queue(input().split(), queue_obj)
    print(f"f_idx: {queue_obj.f_idx}")
    print(f"b_idx: {queue_obj.b_idx}")
    print(f"size: {queue_obj.size()}")
    print(queue_obj.array)