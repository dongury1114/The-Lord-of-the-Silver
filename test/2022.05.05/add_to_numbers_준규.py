# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 우아하게 조지기
        # 재귀로 마지막 값부터 더하고 next
        # 만약 10이 넘으면 전 값을 +1
        prev1 = None
        prev2 = None
        result = ListNode()
        # tmp = 0
        # while l1 is not None or l2 is not None:
        #     prev1, l1, prev1.next = l1, l1.next, prev1
        #     prev2, l2, prev2.next = l2, l2.next, prev2
        #     if (prev1.val+prev2.val)//10 :
        #         tmp += 1
        #     result.val, result.next = (prev1.val+prev2.val)%10, prev1
        
        a = []
        while l1 is not None or l2 is not None:
            prev1, l1, prev1.next = l1, l1.next, prev1
            prev2, l2, prev2.next = l2, l2.next, prev2
            a.append(prev1.val + prev2.val)
            for i in range(len(a)):
                if a[i] >= 10:
                    a[i-1] += 1
                    a[i] = a[i]%10
        result = ListNode()
        while(a):
            pop = a.pop()
            result.val = pop
            result =  
        print(a)
        
            
        
