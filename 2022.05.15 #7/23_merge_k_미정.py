import heapq
lists = [[1,4,5],[1,3,4],[2,6]]
#value 다 뽑아서 list에 담고 
#sorted 한다음에 한 리스트로 만들기
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        root = result = ListNode(None) 
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                #root값을 저장하는데, 중복된 값으로 인한 오류 방지를 위해 추가 인자를 넣는다 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heapq.heappop(heap)#가장 작은 노드의 연결 리스트부터 차례대로 나옴
            idx = node[1]
            result.next = node[2] #
            result = result.next
            print(node, idx, result)
            if result.next:
                heapq.heappush(heap,(result.next.val, idx, result.next))
        return root.next

print(Solution().mergeKLists(lists))