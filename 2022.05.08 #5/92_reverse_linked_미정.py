class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head
        root = start = ListNode(None)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next
        
        for _ in range(right-left):
            tmp,start.next,end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next