nums = [1, 4, 3, 2]
nums.sort(reverse=True)
nums = [0] + nums
res = 0

for i in range(1, len(nums) + 1):
    if i % 2 == 0:
        res += nums[i]
        
print(res)