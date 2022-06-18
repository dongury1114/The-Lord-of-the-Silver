
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1

        return -1
# Runtime: 519 ms, faster than 5.07% of Python online submissions for Binary Search.
# Memory Usage: 14.6 MB, less than 53.80% of Python online submissions for Binary Search.

# 간단 풀이
# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1
# Runtime: 361 ms, faster than 14.06% of Python online submissions for Binary Search.
# Memory Usage: 14.3 MB, less than 98.46% of Python online submissions for Binary Search.
