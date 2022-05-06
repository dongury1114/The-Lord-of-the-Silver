import queue
from typing import Optional



l1 = [2,4,3]
l2 = [5,6,4]

# 풀이 1
# 순서대로 참고해서 리스트에 leftpop 하기
# 합 연산 > 역순으로 linked list 만들기

# 풀이 2 - 그냥 하나씩 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            arr1 = []
            arr2 = []

            while l1 :
                arr1.append(str(l1.val))
                l1 = l1.next
            while l2 :
                arr2.append(str(l2.val))
                l2 = l2.next
            
            arr1 = arr1[::-1]
            arr2 = arr2[::-1]
            result = int(''.join(arr1)) + int(''.join(arr2))
            
            tmp = None
            
            for val in str(result)[::-1]:
                if not tmp:
                    tmp = ListNode(val)
                    head = tmp #첫번째 주소 저장
                else:
                    tmp.next = ListNode(val)
                    tmp = tmp.next

            return head