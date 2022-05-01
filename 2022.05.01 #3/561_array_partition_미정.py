class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()

        ans = 0
        for i in range(len(nums)//2):
            ans += nums[-(i * 2)]

        return ans

