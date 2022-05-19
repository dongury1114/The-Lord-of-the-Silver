from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums).most_common()
        return [s[i][0] for i in range(k)]
