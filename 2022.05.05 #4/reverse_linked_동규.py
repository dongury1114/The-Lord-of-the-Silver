class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        node = None

        while head:
            tmp = head.next
            head.next = node
            node = head
            head = tmp
        return node
