## 시간 초과,,,
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = []
        for i in range(len(nums)-k+1) :
            maxi.append(max(nums[i:i+k]))
        return maxi


##