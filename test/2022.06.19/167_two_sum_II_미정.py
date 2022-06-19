class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(numbers) -1
        mid = (left + right)//2
        ans = 0
        tar = []
        for i in range(len(numbers)):
            while left <= right:
                if numbers[left] + numbers[right] == target:
                    return [left+1, right+1]
                
                elif numbers[left] + numbers[right] < target:
                    left += 1
                elif numbers[left] + numbers[right] > target:
                    right -= 1

# Runtime: 149 ms, faster than 44.11% of Python online submissions for Two Sum II - Input Array Is Sorted.
# Memory Usage: 15 MB, less than 6.46% of Python online submissions for Two Sum II - Input Array Is Sorted.
    