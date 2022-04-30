

nums = [-1,1,0,-3,3]

right=[nums[0]]
left=[nums[-1]]
l = len(nums)
for i in range(1,l-1) :
    right.append(right[i-1]*nums[i])
    left.append(left[i-1]*nums[l-1-i])

# print(right,left)
result =[0]*l
result[0] = left[-1]
result[l-1] = right[-1]
for i in range(1,l-1) :
    result[i] = left[l-2-i] * right[i-1] #인덱스 겁나 헷갈림,,,, 감사합니다요


print(result)