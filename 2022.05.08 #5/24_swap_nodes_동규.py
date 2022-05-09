# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next  # head
            b = a.next
            # prev - a(head) -b - b.next  ->  prev  - b -> a -> b.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a  # 다음으로 넘어가기
        return dummy.next
