from functools import reduce

nums = [-1,1,0,-3,3]

ans = []

#어떻게 자기 자신을 빼고 곱할까?
#나눗셈 활용?
def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

for i in range(len(nums)):
    a = nums[i]
    if a == 0:
        a = 1
        ans.append(int(multiply(nums) / a)) # 0 을 나눌 수 읍다..
    else:
        ans.append(int(multiply(nums) / nums[i])) # 0 을 나눌 수 읍다..

print(ans)