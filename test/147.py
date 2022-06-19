# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결 리스트 -> 배열
        tmp = []
        ans = []
        p = head
        while p:
            tmp.append(p.val)
            p = p.next

        for i in range(1, len(tmp)):
            for j in range(i, 0, -1):
                if tmp[j - 1] > tmp[j]:
                    tmp[j - 1], tmp[j] = tmp[j], tmp[j - 1]

                    # 배열 -> 연결리스트
        p = head

        for i in range(len(tmp)):
            p.val = tmp[i]
            p = p.next
        return head
