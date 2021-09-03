class Que:

    def __init__(self,N):
        self.jul = [0 for i in range(N)]
        self.head = 0
        self.tail = -1

    def push(self, num):


        self.tail += 1
        self.jul[self.tail] = num

    def size(self):

        return self.tail - self.head + 1


    def empty(self):

        if self.size() == 0:
            return 1
        else:
            return 0

    def pop(self):



        if self.empty():
            return -1
        else:
            self.head += 1

            return self.jul[self.head-1]

    def front(self):

        if self.empty():
            return -1
        else:
            return self.jul[self.head]


    def back(self):

        if self.empty():
            return -1
        else:
            return self.jul[self.tail]

N = int(input())
q = Que(N)
for _ in range(N):
    act = input().split()

    if act[0] == 'push':
        num = int(act[-1])
        q.push(num)

    elif 'pop' in act:
        print(q.pop())

    elif 'empty' in act:
        print(q.empty())

    elif 'front' in act:
        print(q.front())

    elif 'back' in act:
        print(q.back())
    elif 'size' in act:
        print(q.size())