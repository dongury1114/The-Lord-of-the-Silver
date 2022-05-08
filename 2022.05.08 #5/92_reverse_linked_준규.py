# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        if not head or left == right:
            return head
        root = start = ListNode(None)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        for _ in range(right-left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        return root.next
#         if left == 1:
#             h = ListNode(None)
#         else:
#             h = head
#         while head:
#             if left == index:
#                 prev = ListNode(None)
#                 while right >= index:
#                     nexte = head.next
#                     head.next = prev
#                     prev = head
#                     head = nexte
#                     index += 1
#                 result = h
#                 while h.next:
#                     h = h.next
#                 h.next = prev
#                 while h:
#                     if h.next.val == None:
#                         h.next = head
#                         break
#                     h = h.next
#                 if left == 1:
#                     result = result.next
#                 return (result)

#             head = head.next
#             index += 1

