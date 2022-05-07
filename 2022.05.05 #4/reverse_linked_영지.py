# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head :
            arr.append(head.val)
            head = head.next
    
        tmp = None
        head = None
        
        arr = arr[::-1]
        
        for val in arr:
            if not tmp:
                tmp = ListNode(val)
                head = tmp #첫번째 주소 저장
            else:
                tmp.next = ListNode(val)#이렇게 안해주면 위 조건문 계속 걸림
                tmp = tmp.next 

        return head


head = [1,2,3,4,5]
linked = None

# for val in head:
#     if not linked:
#         linked = ListNode(val)
#         head = linked #첫번째 주소 저장
#     else:
#         linked.next = ListNode(val)
#         linked = linked.next

# print(Solution.reverseList(head))


class Solution:
    def reverseList( head: Optional[ListNode]) -> Optional[ListNode]:
        node,prev = head,None

        while node :
            next = node.next #node의 다음 주소 임시 저장해두기
            node.next = prev #head 기준 반대로 주소 저장하기

            prev = node #하나씩 뒤로 head이동
            node = next #다음 노드로 이동
            
        return prev
