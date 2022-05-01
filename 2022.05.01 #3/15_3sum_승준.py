# 중복 제거 코드 궁금
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        
        for i in range(len(nums) - 2):
            lt = i + 1
            rt = len(nums) - 1
            
            while lt < rt:
                sum = nums[i] + nums[lt] + nums[rt]
                
                if sum < 0:
                    lt += 1
                elif sum > 0:
                    rt -= 1
                else:
                    if [nums[i], nums[lt], nums[rt]] not in res:
                        res.append([nums[i], nums[lt], nums[rt]])
                        
                    lt += 1
                    rt -= 1
        
        return res