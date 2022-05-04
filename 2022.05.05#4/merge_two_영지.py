# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#배열 떄려넣기
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while list1 :
            arr.append(list1.val)
            list1 = list1.next
        while list2 :
            arr.append(list2.val)
            list2 = list2.next
            
        tmp = None
        head = None

        for val in sorted(arr):
            if not tmp:
                tmp = ListNode(val)
                head = tmp
            else:
                tmp.next = ListNode(val)
                tmp = tmp.next

        return head



# 재귀함수로 풀기
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val) :
            list1 ,list2 = list2, list1
        if list1 :
            list1.next = self.mergeTwoLists(list1.next,list2)
        return list1