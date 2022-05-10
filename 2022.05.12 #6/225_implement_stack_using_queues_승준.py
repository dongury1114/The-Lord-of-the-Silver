from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if self.q:
            return False
        else:
            return True


# from collections import deque

# class MyStack:

#     def __init__(self):
#         self.data = list()

#     def push(self, x: int) -> None:
#         self.data.append(x)

#     def pop(self) -> int:
#         tmp = self.data.pop()
        
#         return tmp

#     def top(self) -> int:
#         tmp = self.data[-1]
#         return tmp

#     def empty(self) -> bool:
#         if self.data:
#             return False
#         else:
#             return True