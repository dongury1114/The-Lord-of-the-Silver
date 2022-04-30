nums = [2,7,11,15]
target = 9

#target 을 nums 에서 2개를 뽑아 만들어라

#sol.01(내풀이)
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])

#sol.02 (yet)

# for i,n in enumerate(nums):
#     complement = target - n
#     # print(complement)

#     if complement in nums[i+1:]:
#         print(nums.index(n), nums[i+1:])

#sol.03
# nums_map ={}
# for i, num in enumerate(nums):
#     nums_map[num] = i

# for i, num in enumerate(nums):
#     if target - num in nums_map and i != nums_map[target - num]:
#         print(i, nums_map[target - num])
nums_map = {}
# 키와 값을 바꿔서 딕셔너리로 저장
for i, num in enumerate(nums):
    nums_map[num] = i
# print(nums_map)
# # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
# for i, num in enumerate(nums):
#     if target - num in nums_map and i != nums_map[target - num]:
#         print([i, nums_map[target - num]])