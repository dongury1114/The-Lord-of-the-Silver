nums = [1,4,3,2]
nums.sort()

s = []

for i in range(len(nums)):
    if i % 2 == 0:
        s.append(nums[i])
print(sum(s))