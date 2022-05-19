from collections import deque

s = "bbbbb"

stack = deque()
count = 0
p = None
for i in s:
    if stack and i in stack:
        count = max(count, len(stack))
        while 1:
            p = stack.popleft()
            if p == i:
                break
    stack.append(i)

<<<<<<< HEAD
count = max(count,len(stack))

print(count)
=======
count = max(count, len(stack))
print(count)
>>>>>>> 6dd12bb4638df0b9b8dc80b6620f27af9386ed1a
