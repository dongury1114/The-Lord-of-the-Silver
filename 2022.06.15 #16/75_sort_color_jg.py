class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i < len(nums):
            j = i
            while j > 0:
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
            i += 1
        return (nums)