class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1

# 이진탐색은 아닌데 재미로 풀어봄
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return nums.index(target) if target in nums else -1
