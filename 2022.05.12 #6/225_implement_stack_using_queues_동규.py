from collections import deque


class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        q = self.queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return not len(self.queue)
