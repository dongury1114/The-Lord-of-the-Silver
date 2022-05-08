from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 처리
        if head == None or head.next == None:
            return head
        
        # 처음 swap만 따로 처리. 리턴될 결과값을 어떻게 지정해줘야 될지 몰라서...
        tmp1 = head
        tmp2 = head.next
        
        head = head.next.next
        tmp2.next = tmp1
        tmp1.next = head
        
        previous = tmp1
        result = tmp2
        
        # 이거 and가 아니라 or로 하면 런타임 에러나는데 왜 그럴까?
        # -> 동규 왈, and로 하면 head까지만 보고 while문을 벗어난다. 하지만 or로 하면 head.next까지 봐버린다. head가 None일 때 head.next는 에러 값이므로 런타임 에러 뜬다.
        # 짝수일 때는 head가 None이 되어서 멈춘다. 홀수일 때는 head.next가 None이 되어서 멈춘다.
        while head and head.next:
            curr1 = head
            curr2 = head.next
            
            head = head.next.next
            curr2.next = curr1
            curr1.next = head
            previous.next = curr2
            
            previous = curr1
            
        return result
        
            