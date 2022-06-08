import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_list = list()

        for i in range(len(nums)):
            heapq.heappush(new_list, -nums[i])

        for j in range(k - 1):
            heapq.heappop(new_list)

        result = -heapq.heappop(new_list)

        return result
