temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

t = temperatures
ans = [0] * len(t)
stack = []
for i, cur in enumerate(t):
    while stack and cur > t[stack[-1]]:
        last = stack.pop()
        ans[last] = i - last
    stack.append(i)
print(ans)


# 시간초과
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         ans = [0] * len(temperatures)

#         for i in range(len(temperatures)):
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     ans[i] = j-i
#                     break
#         return ans
