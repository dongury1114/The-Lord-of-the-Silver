

nums = [-1,0,1,2,-1,-4]

# l = len(nums)
# result = []
# for i in range(l) :
#     for j in range(i+1,l):
#         for k in range(j+1,l) :
#             if nums[i] + nums[j] + nums[k] == 0 :
#                 r = [nums[i], nums[j], nums[k]]
#                 r.sort()
#                 if r not in result : result.append(r)

# print(result)

nums.sort()
result = []
for i in range(len(nums)-2) :
    if i > 0 and nums[i] == nums[i-1] :
        print(i)
        continue
    start = i+1
    end=len(nums)-1
    while start < end :
        r = nums[i] + nums[start] + nums[end]
        if r == 0 :
            if [nums[i],nums[start],nums[end]] not in result : #[-2,0,0,2,2]
                result.append([nums[i],nums[start],nums[end]])
            end -= 1
            start += 1
        elif r > 0 :
            end -= 1
        else :
            start += 1
print(result)