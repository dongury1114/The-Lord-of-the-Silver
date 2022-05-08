from typing import Optional

linked = None
head = [1,2,3,4,5]
left = 2
right = 4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween( head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        t = None
        for _ in range(1,left):
            t = start
            start = start.next

        prev = None
        for _ in range(right-left+1):
            next = start.next
            start.next = prev

            prev = start
            start = next
        if t :
            t.next = prev

        while prev.next :
            prev = prev.next
        prev.next = start
        
        return head

for val in head:
    if not linked:
        linked = ListNode(val)
        head = linked #첫번째 주소 저장
    else:
        linked.next = ListNode(val)
        linked = linked.next

print(Solution.reverseBetween(head,left,right))