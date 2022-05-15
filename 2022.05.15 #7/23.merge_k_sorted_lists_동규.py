# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val

# # sol.01
# def toLinkedList(List):
#     head: ListNode = ListNode()
#     curr = head
#     for r in List:
#         node = ListNode(r)
#         curr.next = node
#         curr = curr.next

#     return head.next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         tmp = []
#         for i in lists:
#             while i:
#                 tmp.append(i.val)
#                 i=i.next
#         tmp = sorted(tmp)
#         return toLinkedList(tmp)

# sol.02
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(0)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next

# 풀이참고: https://byumm315.tistory.com/entry/%EB%A6%AC%ED%8A%B8%EC%BD%94%EB%93%9C-23-Merge-k-Sorted-Lists-1
