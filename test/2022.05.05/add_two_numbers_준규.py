# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 우아하게 조지기
        # 재귀로 마지막 값부터 더하고 next
        # 만약 10이 넘으면 전 값을 +1
        
        prev1 = prev2 = None
        list1 = []
        list2 = []
        while l1 is not None:
            nexte, l1.next = l1.next, prev1
            prev1, l1 = l1, nexte
        while l2 is not None:
            nexte, l2.next = l2.next, prev2
            prev2, l2 = l2, nexte
        while prev1:
            list1.append(prev1.val)
            prev1 = prev1.next
        while prev2:
            list2.append(prev2.val)
            prev2 = prev2.next
        result = str(int(''.join(map(str,list1))) + int(''.join(map(str,list2))))
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
        
