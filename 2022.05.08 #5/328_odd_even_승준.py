from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        result = head
        
        odd = head
        even = head.next
        even_first = head.next
        
        head = head.next.next
        count = 3
        
        while head:
            if count % 2 == 1:
                tmp = ListNode(head.val)
                odd.next = tmp
                odd = odd.next
            else:
                tmp = ListNode(head.val)
                even.next = tmp
                even = even.next
            
            count += 1
            head = head.next
        
        even.next = None
        odd.next = even_first
        
        return result