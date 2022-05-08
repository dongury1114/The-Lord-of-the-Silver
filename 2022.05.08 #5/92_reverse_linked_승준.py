# 미해결
from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        count = 1
        result = head
        previous = head
        if right == 2:
            reverse = head.next
            reverse.next = head
            head.next = None
            result = reverse
        else:
            reverse = None
        
        while count < left:
            previous = head
            head = head.next
            count += 1
            
        if count == left:
            right_before = head
            
        while count <= right:
            tmp = head
            head = head.next
            tmp.next = reverse
            reverse = tmp
            count += 1
            
        if count == right + 1:
            right_after = head
            
        previous.next = reverse
        right_before.next = right_after
        
        return result