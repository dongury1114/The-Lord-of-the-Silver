# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reverse = None
        
        while current is not None:      # 혹은 while head is not None도 가능하다.
            head = head.next
            current.next = reverse
            reverse = current
            current = head
            
        return reverse
            