# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# <런너>
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow.next, reverse, slow = reverse, slow, slow.next
        
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val == reverse.val:
                slow = slow.next
                reverse = reverse.next
                
            else:
                return False
            
        return True

# <리스트>
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         tmp = list()
        
#         while head:
#             value = head.val
#             tmp.append(value)
#             head = head.next
        
#         if len(tmp) == 1:
#             return True
            
#         while len(tmp) > 1:
#             if tmp.pop(0) != tmp.pop():
#                 return False
            
#         return True

# <큐>
# from collections import deque

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         tmp = deque()
        
#         while head:
#             value = head.val
#             tmp.append(value)
#             head = head.next
        
#         if len(tmp) == 1:
#             return True
            
#         while len(tmp) > 1:
#             if tmp.popleft() != tmp.pop():
#                 return False
            
#         return True