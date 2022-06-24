class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return nums and [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
