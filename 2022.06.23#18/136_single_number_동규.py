from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = Counter(nums).most_common()
        result = tmp[-1][0]
        return result


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
