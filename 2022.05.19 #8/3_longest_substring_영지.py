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

count = max(count, len(stack))
print(count)
