from functools import reduce
from collections import deque

#이렇게 멋지게 풀었는데 시간초과? 안해
nums = [-1,1,0,-3,3]
nums=deque(nums)
ans = []
print(nums)
def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

for _ in range(len(nums)):
    tmp = nums.popleft()
    ans.append(multiply(nums))
    nums.append(tmp)
print(ans)


# sol.02(원소곱해서 나누기 실패) -> 문제 잘못봤둠..원래못씀
# ans = []

# #어떻게 자기 자신을 빼고 곱할까?
# #나눗셈 활용?
# def multiply(arr):
#     return reduce(lambda x, y: x * y, arr)

# for i in range(len(nums)):

#     if nums[i] == 0:
#         nums[i] == 1
#         ans.append(int(multiply(nums) / nums[i])) # 0이 곱해져 있기 때문에, 나누기가 소용없다. 원소곱하기 함수는 쓸수가 없다...
#     else:
#         ans.append(int(multiply(nums) / nums[i])) # 0 을 나눌 수 읍다..

# print(ans)