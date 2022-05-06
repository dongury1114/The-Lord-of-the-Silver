# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 두 연결 리스트 모두 리스트로 바꾼다.
        # 리스트를 조합해서 역순으로 바꾼다.
        # 리스트를 더한다.
        # 연결리스트로 변환시켜서 리턴한다.
        
        list1 = list()
        list2 = list()
        
        while l1:
            list1.append(l1.val)
            l1 = l1.next
            
        while l2:
            list2.append(l2.val)
            l2 = l2.next
            
        list1 = list(map(str, list1))
        list2 = list(map(str, list2))
        
        list1 = list1[::-1]
        list2 = list2[::-1]
        
        res = int(''.join(list1)) + int(''.join(list2))
        
        res = list(str(res))[::-1]
        
        head = ListNode(res[0])
        cur = head
        for i in range(1, len(res)):
            tmp = ListNode(res[i])
            cur.next = tmp
            cur = tmp
            
        return head
        