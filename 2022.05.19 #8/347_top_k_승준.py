from collections import defaultdict
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = defaultdict(int)
        heap = list()
        result = list()
        
        for x in nums:
            data[x] += 1
            
        for key, value in data.items():
            heapq.heappush(heap, (-value, key))
            
        for i in range(k):
            tmp = heapq.heappop(heap)
            result.append(tmp[1])
            
        return result

# Solution.topKFrequent(0, nums, 2)