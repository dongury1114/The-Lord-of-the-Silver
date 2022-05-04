from collections import deque
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# def isPalindrome(self, head: ListNode) -> bool:

#     # 데크
head = [1, 2, 2, 1]

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
