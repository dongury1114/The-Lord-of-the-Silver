# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans1,ans2 = [],[]
        node1,node2 = l1,l2
        while node1 != None:
            ans1.append(node1.val)
            node1 = node1.next
        
        while node2 != None:
            ans2.append(node2.val)
            node2 = node2.next
        
        ans1.reverse()
        ans2.reverse()

        fin = []
        
        if len(ans1)< len(ans2):
            for i in range(len(ans1)):
                k = ans1[i] + ans2[i]
                fin.append(k)
            for i in range(i,len(ans2)):
                fin.append(ans2[i])
        else:
            for i in range(len(ans2)):
                k = ans1[i] + ans2[i]
                fin.append(k)
            for i in range(i,len(ans1)):
                fin.append(ans1[i])
                            
        for i in range(len(fin)-1):
            if fin[i] %10==0 : 
                if i == len(fin)-1 and fin[i]>=10:
                    fin.append(fin[i//10])
                else: 
                    fin[i+1]+= fin[i]//10
                    fin[i]=0
        
        cur = dummy = ListNode(0)
        for e in fin:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
            
            
        