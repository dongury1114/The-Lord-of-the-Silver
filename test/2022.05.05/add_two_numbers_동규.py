# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 연결리스트 -> 배열 -> 연결리스트

class Solution:
    def node2list(self, node1: ListNode) -> List:  # linked list -> list
        list1 = []
        while node1 != None:
            list1.append(node1.val)
            node1 = node1.next
        return list1

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2

        list1 = self.node2list(node1)
        list2 = self.node2list(node2)

        list1 = list1[::-1]
        list2 = list2[::-1]

        num1 = int(''.join(str(a) for a in list1))
        num2 = int(''.join(str(a) for a in list2))

        plus = list(str(num1 + num2))
        # plus = self.list2node(plus)
        print(plus)
