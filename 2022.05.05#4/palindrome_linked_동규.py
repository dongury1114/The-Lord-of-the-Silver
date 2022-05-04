from collections import deque


class solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()

        if not head:
            print(True)

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                print(False)

        print(True)
