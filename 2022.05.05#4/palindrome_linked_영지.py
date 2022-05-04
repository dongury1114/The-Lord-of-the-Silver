# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head :
            return True
        
        h = []
        node = head
        while node :
            h.append(node.val)
            node = node.next
            
        if h == h[::-1] :
            return True
        return False
        