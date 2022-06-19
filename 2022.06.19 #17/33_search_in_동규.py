nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

start = 0
end = max(nums)
nums.sort()
while start <= end:
    mid = (start + end) // 2
    a = mid
    if a < target:
        start = mid + 1
    elif a > target:
        end = mid - 1
    else:
        print(mid)
print(-1)
# 이진탐색은 아닌데 재미로 풀어봄
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return nums.index(target) if target in nums else -1
