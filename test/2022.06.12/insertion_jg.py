# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = q = ListNode(0)

        while head:
            while q.next and q.next.val < head.val:
                q = q.next
            q.next, head.next, head = head, q.next, head.next
            if head and q.val > head.val:
                q = root
        
        return root.next
            
