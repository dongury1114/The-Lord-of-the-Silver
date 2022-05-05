# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_list = list()
        
        node = head
        
        while node:
            reverse_list.append(node.val)
            node = node.next
            
        reverse_linked_list = None
        tmp = None
        
        for x in reverse_list[::-1]:
            if reverse_linked_list is None:
                tmp = ListNode(x)
                reverse_linked_list = tmp
            else:
                tmp.next = ListNode(x)
                tmp = tmp.next
                
        return reverse_linked_list
        
        