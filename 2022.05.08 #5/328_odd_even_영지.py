

from typing import Optional


head = []
linked = None
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        add = None
        add_head =  None
        while tmp and tmp.next :
            if not add : 
                add = ListNode(tmp.next.val)
                add_head = add 
            else :
                add.next = ListNode(tmp.next.val)
                add = add.next

            if tmp.next.next == None:
                break
            tmp.next = tmp.next.next
            tmp = tmp.next

        if add_head :
            tmp.next = add_head
        return head



for val in head:
    if not linked:
        linked = ListNode(val)
        head = linked #첫번째 주소 저장
    else:
        linked.next = ListNode(val)
        linked = linked.next

Solution.oddEvenList(head)
print(head.next.next.next.val)


def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return None
        
        tmp = head
        add = head.next
        add_head =  add
        
        while add and add.next :
            tmp.next = tmp.next.next
            tmp = tmp.next
            
            add.next = tmp.next
            add = add.next

            
        tmp.next = add_head
        return head
