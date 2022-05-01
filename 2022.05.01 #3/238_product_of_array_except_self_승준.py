from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = list()
        
        now_left = 1
        for i in range(len(nums)):
            res.append(now_left)
            now_left = now_left * nums[i]
            
        now_right = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = res[j] * now_right
            now_right *= nums[j]
            
        return res