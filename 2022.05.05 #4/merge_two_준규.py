# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        if list1 is None and list2 is None:
            return list1
        while(list1 or list2):
            if not list1:
                arr.append(list2.val)
                list2 = list2.next
                
            elif not list2:
                arr.append(list1.val)
                list1 = list1.next
            else:
                if (list1.val <= list2.val):
                    arr.append(list1.val)
                    list1 = list1.next
                else:
                    arr.append(list2.val)
                    list2 = list2.next
        arr.sort()
        result = ListNode()
        result.val = arr[0]
        head = result
        for i in range(1, len(arr)):
            while(result.next is not None):
                result = result.next
            temp = ListNode()
            temp.val = arr[i]
            result.next = temp
            
        return (head)

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
