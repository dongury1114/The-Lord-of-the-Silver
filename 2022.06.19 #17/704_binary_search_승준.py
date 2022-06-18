class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        left = 0
        right = len(nums) - 1
        result = -1
        
        while left <= right :
            if nums[mid] == target:
                result = mid
                break
                
            elif nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
            
            mid = (left + right) // 2
        
        return result
            