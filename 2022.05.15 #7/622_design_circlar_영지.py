class MyCircularQueue:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0 
        self.cq = [None]*k
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.cq[self.rear] is None:
            self.cq[self.rear] = value
            self.rear =(self.rear + 1) % self.k
            return True
        return False

    def deQueue(self) -> bool:
        if self.cq[self.rear-1] is None:
            return False
        self.cq[self.front] = None
        self.front = (self.front + 1) % self.k
        return True
        
    def Front(self) -> int:
        return -1 if self.cq[self.front] is None else self.cq[self.front]

    def Rear(self) -> int:
        return -1 if self.cq[self.rear-1] is None else self.cq[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.rear == self.front and self.cq[self.front] is None :
            return True
        return False

    def isFull(self) -> bool:
        if self.rear == self.front and self.cq[self.front] is not None  :
            return True
        return False
