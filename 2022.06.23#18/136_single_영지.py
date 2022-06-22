class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        a = 0
        while a != len(nums) :
            if a == len(nums) - 1 : return nums[a]
            if nums[a] == nums[a+1] :
                a += 2
            else : return nums[a]
            