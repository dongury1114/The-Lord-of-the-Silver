class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def a(start, end, nums):
            if start <= end:
                mid = (start+end) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
                return a(start, end, nums)
            else:
                return -1
        start = 0
        end = len(nums) - 1
        return (a(start, end, nums))
    