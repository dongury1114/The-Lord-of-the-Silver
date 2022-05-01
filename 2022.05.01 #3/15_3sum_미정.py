# 소스: https://bellog.tistory.com/137
class Solution(object):
    def threeSum(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복 제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results








#시간 초과

# class Solution(object):
#     def threeSum(self, nums):
#         ans = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 for k in range(len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0 and i != j and j!=k and i!=k:
#                         ans.append( [nums[i],  nums[j] ,nums[k]])
#         for i in ans:
#             i.sort()

#         ans = list(set(tuple(items)for items in ans))
#         ans = [list(items) for items in ans]
#         return ans