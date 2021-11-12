from collections import deque

deque_obj = deque()

print(type(deque_obj))
print(deque_obj)

deque_obj.append(10)
print(deque_obj)
deque_obj.append(20)
print(deque_obj)
deque_obj.appendleft(100)
print(deque_obj)
deque_obj.appendleft(200)
print(deque_obj)

print(deque_obj.pop())
print(deque_obj)
print(deque_obj.popleft())
print(deque_obj)
print(deque_obj.pop())
print(deque_obj)
print(deque_obj.popleft())
print(deque_obj)