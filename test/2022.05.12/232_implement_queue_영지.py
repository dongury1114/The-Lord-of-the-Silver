class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        temp = self.q[0]
        del self.q[0]
        return temp

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if self.q : return False
        return True
