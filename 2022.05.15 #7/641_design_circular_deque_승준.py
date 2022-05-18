class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head, tail을 이용하기 때문에 앞의 문제와 같이 p1, p2가 필요없다. 얼만큼 채워져 있는지를 확인해 Full인지 Empty인지 알기 위해 len과 k(채울 수 있는 노드 최댓값)이 필요하다.
# 연결 리스트의 head와 tail을 통해 노드를 추가하기 때문에 따로 포인터가 필요없다.
# 애초에 앞 공간이 비어있다는 개념 자체가 없다.
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode(None)        
        self.tail = ListNode(None)
        self.k = k
        self.len = 0
        self.head.right = self.tail
        self.tail.left = self.head
    
    def _add(self, node: ListNode, new: ListNode):
        # node.right = new
        # new.left = node
        # self.tail.left = new
        # new.right = self.tail
        
        # 책의 풀이대로라면 n으로 탐색 노드를 지정해줘야, insertFront/insertLast에서 공용으로 _add를 사용할 수 있다.
        # 그렇지 않으면 insertLast의 경우 위처럼 tail이 들어가게 되고, insertFront에서는 head가 들어가게 되어 공용으로 사용할 수 없게 된다.
        n = node.right
        node.right = new
        new.left = node
        n.left = new
        new.right = n
        
    def _del(self, node: ListNode):
        n = node.right
        node.right = n.right
        n.right.left = node
        
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.head, ListNode(value))
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.tail.left, ListNode(value))
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self._del(self.head)
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self._del(self.tail.left.left)
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.len == 0:
            return -1
        return self.head.right.val

    def getRear(self) -> int:
        if self.len == 0:
            return -1
        return self.tail.left.val

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.len == self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()