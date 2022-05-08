# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_l = left = ListNode(None)
        result_r = right = ListNode(None)
        flag = 0
        while head:
            nexte = head.next
            head.next = None
            if not flag:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = nexte
            flag = not flag
        left.next = result_r.next
        return result_l.next
