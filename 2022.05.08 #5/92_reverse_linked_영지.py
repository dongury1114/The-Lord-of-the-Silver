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

        if head == None or head.next == None or left==right :
            return head

        root = ListNode(None)
        root.next = head
        t = root
        
        for _ in range(left-1):
            t = head
            head = head.next

        s = head
        prev = None
        for _ in range(right-left+1):
            next = head.next
            head.next = prev

            prev = head
            head = next


        t.next = prev
        s.next = next

        return root.next



for val in head:
    if not linked:
        linked = ListNode(val)
        head = linked #첫번째 주소 저장
    else:
        linked.next = ListNode(val)
        linked = linked.next

print(Solution.reverseBetween(head,left,right))