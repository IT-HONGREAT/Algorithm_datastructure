
class Stack:

    def __init__(self):

        self.cup = []
        self.height= 0

    def push(self,x):

        self.cup.append(x)
        self.height += 1

    def pop(self):

        if self.height == 0:
            return -1
        else:
            temp = self.cup.pop()
            self.height -= 1
            return temp

    def size(self):

        return self.height

    def empty(self):

        if self.height == 0:
            return 1
        else:
            return 0

    def top(self):

        if self.height == 0:
            return -1
        else:
            return self.cup[-1]


n = int(input())
s = Stack()

for _ in range(n):
    x = input().split()

    if x[0] == 'push':
        s.push(int(x[-1]))

    if 'top' in x:
        print(s.top())

    if 'size' in x:
        print(s.size())

    if 'pop' in x:
        print(s.pop())

    if 'empty' in x:
        print(s.empty())



클래스 밖에서