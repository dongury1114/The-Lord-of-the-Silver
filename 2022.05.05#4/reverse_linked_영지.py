# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head :
            arr.append(head.val)
            head = head.next
    
        tmp = None
        head = None
        
        arr = arr[::-1]
        
        for val in arr:
            if not tmp:
                tmp = ListNode(val)
                head = tmp
            else:
                tmp.next = ListNode(val)
                tmp = tmp.next

        return head