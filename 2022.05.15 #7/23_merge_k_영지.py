# Definition for singly-linked list.
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        que = []
        for i in range(len(lists)) :
            if lists[i] :
                heapq.heappush(que,(lists[i].val,i,lists[i]))  #마지막인자 노드(첫번째)주소를 저장해 줌으로 노드를 전부 해체해서 넣을 필요없다!!!!!!!!!!!!!!!!!!!!!
                
                #인덱스i를 안넣으면 첫번째 인자가 같을때 크기 비교를 할 수 없다. 
                #첫번째 인자가 같을 경우 그 다음 인자로 넘어감. 인덱스 없을 경우 다음인자인 listnode는 크기비교를 할수없어서 오류남
                #인덱스는 중복이 불가하니까 다음 인덱스로 넘어갈 일이없다. 
        
        while que :
            node = heapq.heappop(que)
            index = node[1]
            result.next = node[2]
            
            result = result.next
            if result.next :
                heapq.heappush(que, (result.next.val,index, result.next))
                
        
        return root.next