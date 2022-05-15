# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i, lists[i].next))
        result = temp = ListNode(None)
        while q:
            pop = heapq.heappop(q)
            temp.next = ListNode(pop[0])
            temp = temp.next
            if pop[2]:
                heapq.heappush(q, (pop[2].val, pop[1], pop[2].next))
        return (result.next)
