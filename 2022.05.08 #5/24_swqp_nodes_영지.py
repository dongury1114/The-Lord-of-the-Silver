from typing import Optional


head = [1,2,3,4]
linked = None
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp:
            if tmp.next == None : break
            next = tmp.next
            next.val,tmp.val = tmp.val,next.val
            tmp = next.next

        return head

for val in head:
    if not linked:
        linked = ListNode(val)
        head = linked #첫번째 주소 저장
    else:
        linked.next = ListNode(val)
        linked = linked.next

print(Solution.swapPairs(head))
