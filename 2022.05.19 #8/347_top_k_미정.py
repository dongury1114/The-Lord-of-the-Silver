
class Solution(object):
    def topKFrequent(self, nums, k):
        ans = dict()
        for i in nums:
            ans[i] = 0
        for i in nums:
            ans[i] += 1    

        fin = []
        for _ in range(k):
            max_key = max(ans, key = ans.get)
            fin.append(max_key)
            ans[max_key] = 0
        return fin