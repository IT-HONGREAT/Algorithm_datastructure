class queue:

    def __init__(self,N):

        self.line = [0 for i in range(N)]
        self.head = -1
        self.tail = -1

    def size(self):
        if self.tail - self.head + 1 > 0:

            return (self.tail - self.head) +1

    def empty(self):

        if self.tail < self.head:
            return 1

        else:
            return 0

    def push(self,num):
        if self.head < 0:
            self.head += 1
        self.tail += 1
        self.line[self.tail] = num

    def pop(self):
        if self.empty()==1:
            return -1
        else:
            self.head += 1
            return self.line[self.head]


    def front(self):

        if self.tail <= self.head:
            return -1

        else:
            return self.line[self.head]


    def back(self):

        if self.tail <= self.head:
            return -1

        else:
            return self.line[self.tail]


N = int(input())
q = queue(N)

for _ in range(N):

    order = list(map(str,input().split()))
    # print(order)
    if 'push' in order:
        q.push(int(order[-1]))

    elif 'pop' in order:
        print(q.pop())

    elif 'size' in order:
        print(q.size())

    elif 'empty' in order:
        print(q.empty())

    elif 'front' in order:
        print(q.front())

    elif 'back' in order:
        print(q.back())

