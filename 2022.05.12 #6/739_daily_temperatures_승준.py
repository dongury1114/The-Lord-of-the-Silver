# 시간 초과
from typing import List

# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     stack = [(temperatures[0], 0)]
#     res = [0] * len(temperatures)
    
#     for i in range(1, len(temperatures)):
#         if temperatures[i] > stack[-1][0]:
#             for j in range(len(stack) - 1, -1, -1):
#                 if stack[-1][0] >= temperatures[i]:
#                     continue
                
#                 res[stack[-1][1]] = i - stack[j][1]
#                 stack.pop()
        
#         stack.append((temperatures[i], i))
        
#     return res
                
# print(dailyTemperatures(temperatures))

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
            
        return res