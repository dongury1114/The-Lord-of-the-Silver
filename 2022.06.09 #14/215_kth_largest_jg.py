class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        set_nums = nums
        q = []
        for i in list(set_nums):
            heapq.heappush(q, -i)
        for _ in range(k):
            result = heapq.heappop(q)
            
        return(-result)
