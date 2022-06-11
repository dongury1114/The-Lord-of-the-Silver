# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        a_list = []
        while head != None :
            a_list.append(head.val)
            head = head.next
            
        if not a_list : return None
        a_list.sort()
        
        temp = ListNode(a_list[0])
        root = temp
        for i in range(1,len(a_list)) :
            temp.next = ListNode()
            temp = temp.next
            temp.val = a_list[i]
 

        return root